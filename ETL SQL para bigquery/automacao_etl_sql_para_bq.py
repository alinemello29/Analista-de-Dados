# -*- coding: utf-8 -*-
"""automacao_etl_sql_para_bq

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/149equOHTMUCAPGD5SMP987aUg5teJqJu
"""

!curl ipecho.net/plain

!pip install mysql-connector-python

# Importando as bibliotecas necessárias
import mysql.connector
import pandas as pd
from google.cloud import bigquery
import requests
import os

# URL pública para a chave de serviço JSON
json_key_url = 'https://storage.googleapis.com/chaves-01/etl-bq/projeto-aline-440013-87e1b1daa2fa.json'
local_json_path = '/tmp/service_account_key.json'

def download_key_from_url():
    """Função para baixar a chave JSON de uma URL pública"""
    response = requests.get(json_key_url)
    if response.status_code == 200:
        with open(local_json_path, 'wb') as f:
            f.write(response.content)
        print("Chave JSON baixada com sucesso da URL pública.")
    else:
        print("Falha ao baixar a chave JSON. Verifique a URL.")

# Baixar a chave JSON
download_key_from_url()

# Inicializando o cliente BigQuery com a chave JSON diretamente
client = bigquery.Client.from_service_account_json(local_json_path)

# Variáveis de conexão MySQL
db_config = {
    "host": "34.69.233.123",
    "user": "root",
    "password": "",
    "database": "loja",
}

# Definindo as variáveis com id do projeto e nome do dataset
project_id = 'projeto-aline-440013'
dataset_id = 'loja_python_otimizado'

def fetch_and_load_to_bigquery(query, table_name):
    # Conexão com MySQL, executando as consultas, e convertendo para DataFrame
    with mysql.connector.connect(**db_config) as conn:
        df = pd.read_sql(query, conn)
    # Carregando os DataFrames na BigQuery
    df.to_gbq(f"{project_id}.{dataset_id}.{table_name}", project_id=project_id,
              if_exists='replace', credentials=client._credentials)
    print(f"Loaded {table_name} to BigQuery successfully.")

# Definindo as queries e seus respectivos nomes de tabela na BigQuery
queries = {
    "cliente": "SELECT * FROM Cliente;",
    "pedido": "SELECT * FROM Pedido;",
    "produto": "SELECT * FROM Produto;",
    "item_pedido": "SELECT * FROM ItemPedido;",
    "categoria": "SELECT * FROM Categoria;",
    "produto_pedido": "SELECT * FROM ProdutoCategoria;"
}

# Executando o código para cada tabela existente no banco transacional
for table_name, query in queries.items():
    fetch_and_load_to_bigquery(query, table_name)