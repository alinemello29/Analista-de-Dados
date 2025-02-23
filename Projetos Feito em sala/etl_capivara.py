# -*- coding: utf-8 -*-
"""etl_capivara

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VaTgspchS5xfujUDV71qHmv69Y2QaXgf
"""

import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQ3-zccoyCwJZ1GeVdcHq9VYOFb_xA-sGeib9v6B54tws94wdfGaNFn_EkZCTZgnAgBcHxk55eBL_1J/pub?gid=348262062&single=true&output=csv')
df.info()

df.rename(columns={'Data':'data','Receita':'receita','Custo':'custo',
'Lucro':'lucro','Quantidade de Vendas':'qtde','Novos Clientes':'nclientes',
'Categoria do Produto':'categoria','Satisfação do Cliente':'satisfacao',
'Região':'regiao'},inplace=True)

df.head()

from google.colab import files
from google.cloud import bigquery
from google.colab import auth


# Autenticar no Google Cloud
auth.authenticate_user()

# Criar o cliente do BigQuery
client = bigquery.Client()

# Definir o ID do projeto e o ID da tabela
project_id = 'turmas-dados'
table_id = 'turmas-dados.capivara.dados'

# Enviar o DataFrame para o BigQuery
df.to_gbq(table_id, project_id=project_id, if_exists='replace')