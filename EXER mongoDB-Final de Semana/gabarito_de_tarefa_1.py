# -*- coding: utf-8 -*-
"""Gabarito de Tarefa 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GMj424vrd3WOKUM_trv-CGC691Q60nLE
"""

'''
Crie um processo de etl completo (Pipeline)
que cumpra as seguintes tarefas em um único ipynb:

1 - usando a api pública do mercado livre traga todos
os resultados de uma consulta sobre um termo específico para o ambiente
Python

2 - Armazene os resultados dessa busca em um df pandas

3 - Faça as transformações que julgar necessárias no dtaframe
Ex.: mudar nomes de colunas, mudar tipos de dados, remover dados nulos,
criar novas colunas e etc...

4 - Salve os arquivo em formato csv.

5 - Envie os arquivo csv para um bucket chamado mercadolivre_seunome

6 - Converta o arquivo csv em coleções e os envie para o ATLAS/MongoDB

7 - Crie um database SQL chamado mercado em sua instância e abasteça esse
db com os dados dos arquivo csv.

8 - Crie uma conexão entre o Cloud SQL e a bigquery para enviar os dados
do banco mecado para um conjunto de dados chamado mercado_livre na BQ

9 - Envie os arquivo csv do colab para outro conjunto de dados da BQ chamado
mercado2

10 - Conecte os arquivo do dataset mercado com um relatório no looker studio
'''

!pip install mysql.connector

!pip install pymongo

!curl ipecho.net/plain

import pandas as pd
import mysql.connector
from mysql.connector import Error
import requests

'''
1 - usando a api pública do mercado livre traga todos
os resultados de uma consulta sobre um termo específico para o ambiente
Python

2 - Armazene os resultados dessa busca em um df pandas

'''

# Termo de busca
termo_de_busca = "webcam"

# URL da API do Mercado Livre
url = f"https://api.mercadolibre.com/sites/MLB/search?q={termo_de_busca}"

# Fazer a requisição GET
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Carregar os dados em formato JSON
    dados = response.json()

    # Extrair os dados relevantes
    produtos = []
    for item in dados.get('results', []):
        produto = {
            "Título": item.get('title'),
            "Preço (R$)": item.get('price'),
            "Link": item.get('permalink'),
            "Condição": item.get('condition'),
            "Categoria": item.get('category_id')
        }
        produtos.append(produto)

    # Criar o DataFrame
    df = pd.DataFrame(produtos)

    # Exibir o DataFrame
    display(df)
else:
    print(f"Erro na requisição: {response.status_code}")

'''
3 - Faça as transformações que julgar necessárias no dtaframe
Ex.: mudar nomes de colunas, mudar tipos de dados, remover dados nulos,
criar novas colunas e etc...
'''
display(df.head(1))
df.rename(columns={'Título':'produto','Preço (R$)':'valor','Link':'link',
                   'Condição':'condicao','Categoria':'categoria'},inplace=True)
df.head(1)

'''
4 - Salve os arquivo em formato csv.
'''
df.to_csv('mercado.csv',index=False)

'''
5 - Envie os arquivo csv para um bucket chamado mercadolivre_seunome
'''
from google.colab import auth
auth.authenticate_user()
project_id = "turmas-dados"
!gcloud config set project {project_id}
from google.cloud import storage
client = storage.Client()
bucket_name = "etl-basico"
bucket = client.bucket(bucket_name)
#df.to_csv('df_tratado.csv', index=False)
from google.cloud import storage
# Nome do arquivo no GCS
destination_blob_name = 'mercadolivre_douglas/mercado.csv'
# Caminho do arquivo local
source_file_name = 'mercado.csv'
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)
print(f'File {source_file_name} uploaded to {destination_blob_name}.')

# Tutorial de apoio para questão 6
from IPython.display import HTML

video_id = "sCGvcS4I0QA"  # ID do vídeo
video_url = f"https://www.youtube.com/embed/{video_id}"

HTML(f"""
<iframe width="560" height="315" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
""")

'''
6 - Converta o arquivo csv em coleções e os envie para o ATLAS/MongoDB
'''
from pymongo import MongoClient
import pandas as pd
# Conectar ao MongoDB Atlas
client = MongoClient('mongodb+srv://douglasdealmeidaribeiro:c2ygnygvNLpGtOZr@cluster0.xu3hl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['mercado']  # Nome do banco de dados
webcam = df
webcam = webcam.to_dict(orient='records')
db.webcam.insert_many(webcam)

# Tutorial de apoio para questão 7
from IPython.display import HTML

video_id = "vUBkZLpLjq4"  # ID do vídeo
video_url = f"https://www.youtube.com/embed/{video_id}"

HTML(f"""
<iframe width="560" height="315" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
""")

'''
7 - Crie um database SQL chamado mercado em sua instância e abasteça esse
db com os dados dos arquivo csv.
'''
# Configuração da conexão com o MySQL
config = {
    'user': 'root',
    'password': '',
    'host': '34.70.26.188',
    'database': 'mercado'
}

try:
    # Conexão com o banco de dados
    conn = mysql.connector.connect(**config)
    if conn.is_connected():
        print("Conexão bem-sucedida ao banco de dados!")

        # Criar um cursor
        cursor = conn.cursor()

        # Criar a tabela (se necessário)
        criar_tabela_query = """
        CREATE TABLE IF NOT EXISTS webcam (
            produto VARCHAR(255),
            valor DECIMAL(11,2),
            link VARCHAR(255),
            condicao VARCHAR(255),
            categoria VARCHAR(255)
        );
        """
        cursor.execute(criar_tabela_query)

        # Inserir os dados do DataFrame no banco de dados
        for _, row in df.iterrows():
            insert_query = """
            INSERT INTO webcam (produto, valor, link, condicao, categoria)
            VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(insert_query, tuple(row))

        # Confirmar as mudanças no banco de dados
        conn.commit()
        print("Dados enviados com sucesso!")

except Error as e:
    print("Erro ao conectar ao banco de dados:", e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão encerrada.")

# Etapa resolvida diretamente no console da GCP
'''
8 - Crie uma conexão entre o Cloud SQL e a bigquery para enviar os dados
do banco mecado para um conjunto de dados chamado mercado_livre na BQ
'''
from IPython.display import HTML

video_id = "b_wnU2SuVoM"  # ID do vídeo
video_url = f"https://www.youtube.com/embed/{video_id}"

HTML(f"""
<iframe width="560" height="315" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
""")

'''
9 - Envie os arquivo csv do colab para outro conjunto de dados da BQ chamado
mercado2
'''
from google.colab import files
from google.cloud import bigquery
from google.colab import auth


# Autenticar no Google Cloud
auth.authenticate_user()

# Criar o cliente do BigQuery
client = bigquery.Client()

# Definir o ID do projeto e o ID da tabela
project_id = 'turmas-dados'
table_id = 'turmas-dados.mercado2.webcam'

# Enviar o DataFrame para o BigQuery
df.to_gbq(table_id, project_id=project_id, if_exists='replace')

# Etapa resolvida diretamente no gcp console
'''
10 - Conecte os arquivo do dataset mercado com um relatório no looker studio
'''

from IPython.display import HTML

video_id = "tXzGbgPA6Wc"  # ID do vídeo
video_url = f"https://www.youtube.com/embed/{video_id}"

HTML(f"""
<iframe width="560" height="315" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
""")

# Material Extra sobre looker studio

from IPython.display import HTML

video_id = "0WnarOe1CWo"  # ID do vídeo
video_url = f"https://www.youtube.com/embed/{video_id}"

HTML(f"""
<iframe width="560" height="315" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
""")