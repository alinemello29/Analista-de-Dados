# -*- coding: utf-8 -*-
"""conexão faculdade

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14aZa99psBDLIrpjEe5AvpC0DOSxvHsa4
"""

!pip install mysql-connector-python

import mysql.connector
import pandas as pd

host = '34.66.48.131'
user = 'root'
password = ''
database = 'faculdade'

!curl ipecho.net/plain

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
) # estas linhas servem para criar a conexão com o banco de dados
cursor = connection.cursor() #criando o cursor para apontar para o banco de dados
query = 'show tables;' # Query ou consulta desejada
cursor.execute(query) # Execução da consulta
result = cursor.fetchall() # armazenando os resultados na variável results
tabelas = pd.DataFrame(result,columns=cursor.column_names) # convertendo a variável result em um df pandas chamado tabelas
display(tabelas) # exibindo a tabela pandas
cursor.close() # fechando o cursor
connection.close() # fechando a conexão

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
) # estas linhas servem para criar a conexão com o banco de dados
cursor = connection.cursor() #criando o cursor para apontar para o banco de dados
query = '''
SELECT * FROM Aluno;
''' # Query ou consulta desejada
cursor.execute(query) # Execução da consulta
result = cursor.fetchall() # armazenando os resultados na variável results
aluno = pd.DataFrame(result,columns=cursor.column_names) # convertendo a variável result em um df pandas chamado tabelas
display(aluno) # exibindo a tabela pandas
cursor.close() # fechando o cursor

'''
Fazendo o uploado do arquivo tratado diretamente pelo
Colab, sem passra pela máquina local
'''
from google.colab import auth
auth.authenticate_user()
project_id = 'projeto-aline-440013'
!gcloud config set project {project_id}
from google.cloud import storage
client = storage.Client()
bucket_name = 'teste-aline'
bucket = client.bucket(bucket_name)
aluno.to_csv('faculdade_aluno.csv',index=False)
#from google.cloud import storage
destination_blob_name = 'banco-faculdade/faculdade_aluno.csv'
source_file_name = 'faculdade_aluno.csv'
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
) # estas linhas servem para criar a conexão com o banco de dados
cursor = connection.cursor() #criando o cursor para apontar para o banco de dados
query = '''
SELECT * FROM Curso;
''' # Query ou consulta desejada
cursor.execute(query) # Execução da consulta
result = cursor.fetchall() # armazenando os resultados na variável results
curso = pd.DataFrame(result,columns=cursor.column_names) # convertendo a variável result em um df pandas chamado tabelas
display(curso) # exibindo a tabela pandas
cursor.close() # fechando o cursor
connection.close() # fechando a conexão

'''
Fazendo o uploado do arquivo tratado diretamente pelo
Colab, sem passra pela máquina local
'''
from google.colab import auth
auth.authenticate_user()
project_id = 'projeto-aline-440013'
!gcloud config set project {project_id}
from google.cloud import storage
client = storage.Client()
bucket_name = 'teste-aline'
bucket = client.bucket(bucket_name)
aluno.to_csv('faculdade_curso.csv',index=False)
#from google.cloud import storage
destination_blob_name = 'banco-faculdade/faculdade_curso.csv'
source_file_name = 'faculdade_curso.csv'
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
) # estas linhas servem para criar a conexão com o banco de dados
cursor = connection.cursor() #criando o cursor para apontar para o banco de dados
query = '''
SELECT * FROM Departamento;
''' # Query ou consulta desejada
cursor.execute(query) # Execução da consulta
result = cursor.fetchall() # armazenando os resultados na variável results
departamento = pd.DataFrame(result,columns=cursor.column_names) # convertendo a variável result em um df pandas chamado tabelas
display(departamento) # exibindo a tabela pandas
cursor.close() # fechando o cursor
connection.close() # fechando a conexão

'''
Fazendo o uploado do arquivo tratado diretamente pelo
Colab, sem passra pela máquina local
'''
from google.colab import auth
auth.authenticate_user()
project_id = 'projeto-aline-440013'
!gcloud config set project {project_id}
from google.cloud import storage
client = storage.Client()
bucket_name = 'teste-aline'
bucket = client.bucket(bucket_name)
aluno.to_csv('faculdade_departamento.csv',index=False)
#from google.cloud import storage
destination_blob_name = 'banco-faculdade/faculdade_departamento.csv'
source_file_name = 'faculdade_departamento.csv'
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
) # estas linhas servem para criar a conexão com o banco de dados
cursor = connection.cursor() #criando o cursor para apontar para o banco de dados
query = '''
SELECT * FROM Disciplina;
''' # Query ou consulta desejada
cursor.execute(query) # Execução da consulta
result = cursor.fetchall() # armazenando os resultados na variável results
disciplina = pd.DataFrame(result,columns=cursor.column_names) # convertendo a variável result em um df pandas chamado tabelas
display(disciplina) # exibindo a tabela pandas
cursor.close() # fechando o cursor
connection.close() # fechando a conexão

'''
Fazendo o uploado do arquivo tratado diretamente pelo
Colab, sem passra pela máquina local
'''
from google.colab import auth
auth.authenticate_user()
project_id = 'projeto-aline-440013'
!gcloud config set project {project_id}
from google.cloud import storage
client = storage.Client()
bucket_name = 'teste-aline'
bucket = client.bucket(bucket_name)
aluno.to_csv('faculdade_disciplina.csv',index=False)
#from google.cloud import storage
destination_blob_name = 'banco-faculdade/faculdade_disciplina.csv'
source_file_name = 'faculdade_disciplina.csv'
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
) # estas linhas servem para criar a conexão com o banco de dados
cursor = connection.cursor() #criando o cursor para apontar para o banco de dados
query = '''
SELECT * FROM Matricula;
''' # Query ou consulta desejada
cursor.execute(query) # Execução da consulta
result = cursor.fetchall() # armazenando os resultados na variável results
matricula = pd.DataFrame(result,columns=cursor.column_names) # convertendo a variável result em um df pandas chamado tabelas
display(matricula) # exibindo a tabela pandas
cursor.close() # fechando o cursor
connection.close() # fechando a conexão

'''
Fazendo o uploado do arquivo tratado diretamente pelo
Colab, sem passra pela máquina local
'''
from google.colab import auth
auth.authenticate_user()
project_id = 'projeto-aline-440013'
!gcloud config set project {project_id}
from google.cloud import storage
client = storage.Client()
bucket_name = 'teste-aline'
bucket = client.bucket(bucket_name)
aluno.to_csv('faculdade_matricula.csv',index=False)
#from google.cloud import storage
destination_blob_name = 'banco-faculdade/faculdade_matricula.csv'
source_file_name = 'faculdade_matricula.csv'
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
) # estas linhas servem para criar a conexão com o banco de dados
cursor = connection.cursor() #criando o cursor para apontar para o banco de dados
query = '''
SELECT * FROM Nota;
''' # Query ou consulta desejada
cursor.execute(query) # Execução da consulta
result = cursor.fetchall() # armazenando os resultados na variável results
nota = pd.DataFrame(result,columns=cursor.column_names) # convertendo a variável result em um df pandas chamado tabelas
display(nota) # exibindo a tabela pandas
cursor.close() # fechando o cursor
connection.close() # fechando a conexão

'''
Fazendo o uploado do arquivo tratado diretamente pelo
Colab, sem passra pela máquina local
'''
from google.colab import auth
auth.authenticate_user()
project_id = 'projeto-aline-440013'
!gcloud config set project {project_id}
from google.cloud import storage
client = storage.Client()
bucket_name = 'teste-aline'
bucket = client.bucket(bucket_name)
aluno.to_csv('faculdade_notas.csv',index=False)
#from google.cloud import storage
destination_blob_name = 'banco-faculdade/faculdade_notas.csv'
source_file_name = 'faculdade_notas.csv'
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
) # estas linhas servem para criar a conexão com o banco de dados
cursor = connection.cursor() #criando o cursor para apontar para o banco de dados
query = '''
SELECT * FROM Professor;
''' # Query ou consulta desejada
cursor.execute(query) # Execução da consulta
result = cursor.fetchall() # armazenando os resultados na variável results
professor = pd.DataFrame(result,columns=cursor.column_names) # convertendo a variável result em um df pandas chamado tabelas
display(professor) # exibindo a tabela pandas
cursor.close() # fechando o cursor
connection.close() # fechando a conexão