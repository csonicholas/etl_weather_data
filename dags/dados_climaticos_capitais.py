import os
import pendulum
import pandas as pd
from airflow import DAG 
from os.path import join
from datetime import datetime
from dotenv import load_dotenv
from locations import locations
from airflow.macros import ds_add
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

load_dotenv()
api_key = os.getenv('API_KEY')

with DAG(
    "dados_climaticos_capitais",
    start_date= pendulum.datetime(2023, 9, 15, tz="UTC"),
    schedule_interval='0 0 * * 1', # executar toda segunda feira
) as dag:
    
    def extract_data(data_interval_end):
                    
        urls = []
        url_base = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

        for location in locations:
            url = join(url_base,
            f'{location}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&lang=pt&include=days&key={api_key}&contentType=csv')
            urls.append(url)
        df_raw_data = pd.DataFrame() 

        for url in urls:
            print(url)    
            df = pd.read_csv(url)  
            df_raw_data = pd.concat([df_raw_data, df], ignore_index=True)

        return df_raw_data
        
       
    def transform_data(df_raw_data):

        columns_name = ['name', 'datetime', 'tempmax', 'tempmin', 'conditions', 'description']
        df = df_raw_data[columns_name]
        df = df.rename(columns={'name': 'Cidades', 'datetime': 'Data', 'tempmax': 'Temp. Máx.', 'tempmin': 'Temp. Mín.',
         'conditions':'Condições', 'description':'Descrição'})

        return df
           

    def load_data(data_interval_end,df_raw_data,df):

        file_path = f'/home/csonicholas/Documents/ubuntu/airflow/Capitais/{data_interval_end}/'

        df_raw_data.to_csv(file_path + 'raw_data.csv')
        df.to_csv(file_path + 'spec_data.csv')


    def etl(data_interval_end):

        df_raw_data = extract_data(data_interval_end)
        df = transform_data(df_raw_data)
        load_data(data_interval_end,df_raw_data,df)



    task_1 = BashOperator(
        task_id = 'new_folder',
        bash_command = 'mkdir -p "/home/csonicholas/Documents/ubuntu/airflow/Capitais/{{data_interval_end.strftime("%Y-%m-%d")}}"'
    )


    task_2 = PythonOperator(
        task_id = 'etl',
        python_callable = etl,
        op_kwargs = {'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'}
    )

    task_1 >> task_2 