# -*- coding: utf-8 -*-
"""Tarefa 1 - Aline

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ji5vn9qvX0tYBvpaCz-ypP-wVGz4oCtU
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

4 - Salve os arquivos em formato csv.

5 - Envie os arquivos csv para um bucket chamado mercadolivre_seunome

6 - Converta os arquivos csv em coleções e os envie para o ATLAS/MongoDB

7 - Crie um database SQL chamado mercado em sua instância e abasteça esse
db com os dados dos arquivos csv.

8 - Crie uma conexão entre o Cloud SQL e a bigquery para enviar os dados
do banco mecado para um conjunto de dados chamado mercado_livre na BQ

9 - Envie os arquivos csv do colab para outro conjunto de dados da BQ chamado
mercado2

10 - Conecte os arquivos do dataset mercado com um relatório no looker studio
'''

import requests
import pandas as pd

def fetch_data(termo_de_busca):
    response = requests.get(f"https://api.mercadolibre.com/sites/MLB/search?q={termo_de_busca}")
    response.raise_for_status()
    return response.json()['results']

termo_de_busca = 'notebook'

try:
    results = fetch_data(termo_de_busca)
    print("Resultados da API:", results)
except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro: {e}")

df = pd.DataFrame(results)

df.rename(columns={
    'id': 'Item ID',
    'title': 'Título',
    'price': 'Preço',
    'currency_id': 'Moeda',
    'condition': 'Condição',
    'available_quantity': 'Quantidade Disponível'
}, inplace=True)

df['Preço'] = df['Preço'].astype(float)

df.dropna(inplace=True)

csv_file_path = 'resultados_mercadolivre.csv'
df.to_csv(csv_file_path, index=False)

print(f"Arquivo CSV salvo em: {csv_file_path}")

# 1. Instalação da biblioteca
!pip install google-cloud-storage

# 2. Autenticação no Google Cloud
from google.colab import auth
auth.authenticate_user()

# 3. Definir o ID do projeto
project_id = 'projeto-aline-440013'  # Substitua pelo seu ID do projeto
!gcloud config set project {project_id}

# 4. Importar a biblioteca de armazenamento
from google.cloud import storage

# 5. Criar um cliente de armazenamento
client = storage.Client()

# 6. Nome do bucket
bucket_name = 'mercadolivre_alinemelo'  # Nome do seu bucket
bucket = client.bucket(bucket_name)

# 7. Definir o caminho do arquivo local
local_file_path = 'resultados_mercadolivre.csv'  # O caminho do arquivo que você deseja enviar

# 8. Verificar se o arquivo existe
import os

if not os.path.exists(local_file_path):
    print(f"O arquivo {local_file_path} não foi encontrado.")
else:
    # 9. Definir o caminho do blob de destino
    destination_blob_name = 'tabela/resultados_mercadolivre.csv'  # Caminho no bucket

    # 10. Criar um objeto blob e fazer o upload
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(local_file_path)

    print(f"Arquivo {local_file_path} enviado para o bucket {bucket_name} como {destination_blob_name}.")

# 1. Instalação da biblioteca pymongo
!pip install pymongo

# 2. Importar bibliotecas
import pandas as pd
from pymongo import MongoClient

# 3. Conectar ao MongoDB Atlas
CONNECTION_STRING = "mongodb+srv://alinemelo:U8h8JxUt3tcZujmU@cluster0.0rnwx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Substitua com suas credenciais
client = MongoClient(CONNECTION_STRING)

# 4. Criar ou acessar o banco de dados e a coleção
db = client['mercadolivre']  # Nome do banco de dados
collection = db['aline']  # Nome da coleção

# 5. Criar um DataFrame e inserir dados
data = {
    'nome': ['Alice', 'Bob', 'Charlie'],
    'idade': [30, 25, 35]
}
df = pd.DataFrame(data)

# Converter DataFrame em dicionários
data_dict = df.to_dict("records")

# Instalar a biblioteca sqlite3 (geralmente já está incluída)
!pip install sqlite3

import sqlite3
import pandas as pd
from google.colab import files

# 1. Conectar ao banco de dados (cria um novo se não existir)
conn = sqlite3.connect('mercado.db')

# 2. Criar um cursor
cursor = conn.cursor()

# 3. Criar uma tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
''')

# 4. Confirmar a criação da tabela
conn.commit()