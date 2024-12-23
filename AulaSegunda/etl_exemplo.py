# -*- coding: utf-8 -*-
"""etl_exemplo

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZA9lwsqq0mitZwD1H2Z1niv60cawRTAH
"""

import pandas as pd

df = pd.read_csv('https://storage.cloud.google.com/aula-6-aline/dados%20brutos/dados.csv')
print(df)

df['imc'] = df['peso'] / df['altura']**2
print(df)

display(df)

df.info()

'''
verficamos que ao extrair os dados, os mesmo
vieram limpos e tipados corretamente, porém,
desaejamos fazer uma transformação criando uma coluna que
calcula automaticamente os valores de imc
'''

df['imc'] = df['peso'] / df['altura']**2
display(df)

imcs = df['imc']
imcs = list(imcs)
for i in range(len(imcs)):
  imcs[i] = round(imcs[i],2)
df['imc'] = imcs
display(df)

df.to_csv('tratados.csv' ,index=False)

'''
fazendo o upload do arquivo tratado diretamente pelo colab,
sen passar pela maquina local
'''

from google.colab import auth
auth.authenticate_user()
project_id = 'projeto-aline-440013'
!gcloud config set project {project_id}
from google.cloud import storage
client = storage.Client()
bucket_name = 'aula-6-aline'
bucket = client.bucket(bucket_name)
df.to_csv('tratados.csv',index=False)
from google.cloud import storage
destination_blob_name = 'dados-tratados/tratados.csv'
source_file_name = 'tratados.csv'
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)

df

# selecionando as informações da coluna autura
df['altura']

#Armazenando as informações da coluna altura em uma variável chamada alturas
alturas = df['altura']
display(alturas)

# Vericicando o tipo
type(alturas)

# transformando o objeto em uma lista
alturas = list(alturas)
type(alturas)

print(alturas)

alturas[0] = 1.86

print(alturas)

# Devolvendo os dados de alturas para a coluna de altura do df
df['altura'] = alturas

display(df)