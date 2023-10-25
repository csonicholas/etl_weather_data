# etl_weather_data
Projeto usando Apache Airflow para obtenção de Dados climáticos das capitais brasileiras

Compartilho um projeto que possibilitou colocar em prática os estudos do Apache Airflow. Foram utilizadas as seguintes tecnologias neste projeto:



◾ Apache Airflow

◾Linguagem de programação Python

◾Power BI



Neste projeto, o objetivo foi desenvolver um processo de ETL (Extração, Transformação e Carregamento) com o Airflow, a partir dos dados meteorológicos dos próximos 7 dias das capitais brasileiras a partir da Visual Crossing: Weather Data & API https://www.visualcrossing.com/weather-api. 



Algumas das aplicações desses dados são:

◾Empresas de turismo - Agendar passeios de acordo com a previsão do tempo para a semana.

◾Programas de TV - Com os dados é possível fazer quadros de previsão do tempo.



O Apache Airflow foi utilizado para agendar um horário específico da semana para realizar o processo ETL. Os dados da API vão ser consumidos, tratados e carregados para uma base da dados. 

Um simples dashboard foi feito como forma de demonstrar algumas das aplicações.
https://app.powerbi.com/view?r=eyJrIjoiOTViNDhlODgtMjExOC00Mzk3LWFkNDQtNGRlZWYwNjkxM2U1IiwidCI6IjhjMjRmYmZiLWEzNGQtNGI3Yy1iZDEzLTEzMWEwMmIyNGUzNSJ9

Alterações podem ser feitas para adequar-se a necessidade de cada usuário, como salvar os dados diretamente em algum serviço de cloud, como o Amazon S3, por exemplo.
