from unidecode import unidecode
locations =['Aracaju',
            'Belo Horizonte',
            'Belém',
            'Boa Vista',
            'Brasília',
            'Campo Grande',
            'Cuiabá',
            'Curitiba',
            'Florianópolis',
            'Fortaleza',
            'Goiânia',
            'João Pessoa',
            'Macapá',
            'Maceió',
            'Manaus',
            'Natal',
            'Palmas',
            'Porto Alegre',
            'Porto Velho',
            'Recife',
            'Rio Branco',
            'Rio de Janeiro',
            'Salvador Bahia',
            'São Luís',
            'São Paulo',
            'Teresina',
            'Vitória'
            ]
locations = [unidecode(location).replace(' ', '%20') for location in locations] 