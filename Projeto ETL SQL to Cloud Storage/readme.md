# 🚀 Projeto ETL SQL to Cloud Storage

## 📖 Descrição
Este projeto tem como objetivo realizar a extração, transformação e carregamento (ETL) de dados de um banco de dados MySQL no Google Cloud SQL para o Google Cloud Storage. Utilizaremos o Google Colab para conectar e manipular os dados.

## 🛠️ Tecnologias Utilizadas
- **Google Cloud Platform** ☁️
- **MySQL** 🐬
- **Python** 🐍
- **Pandas** 📊
- **Google Cloud Storage** 🗄️
- **Google Colab** 📚

## 📋 Passos do Projeto

1. **Criar uma Instância MySQL**
   - Acesse o [Google Cloud SQL](https://cloud.google.com/sql).
   - Crie uma nova instância MySQL.

2. **Criar um Banco de Dados**
   - No MySQL, crie um banco de dados chamado `loja`.

3. **Popular o Banco de Dados**
   - Use os dados disponíveis no arquivo deste [link](https://colab.research.google.com/drive/18--jmuhLkQbKsJ5jJdI8W6y0ManYtr0r?usp=sharing) para popular o banco de dados `loja`.

4. **Conectar ao Banco de Dados no Google Colab**
   - Crie um novo notebook no Google Colab.
   - Utilize o código abaixo para conectar ao banco de dados e trazer todas as informações:

   ```python
   import mysql.connector
   import pandas as pd

   # Conexão com o banco de dados
   conn = mysql.connector.connect(
       host='SEU_IP_DO_BANCO',
       user='SEU_USUARIO',
       password='SUA_SENHA',
       database='loja'
   )

   # Carregar todas as tabelas em DataFrames
   tabelas = pd.read_sql("SHOW TABLES", conn)
   for tabela in tabelas.values:
       df = pd.read_sql(f"SELECT * FROM {tabela[0]}", conn)
       print(df)

   # Fechar a conexão
   conn.close()
Enviar Tabelas para o Google Cloud Storage
Crie um bucket no Google Cloud Storage chamado loja.
Dentro do balde, crie uma pasta chamada tabelas.
Utilize o seguinte código para enviar as tabelas:
Pitão

Copiar
from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('loja')

for tabela in tabelas.values:
    df.to_csv(f'tabelas/{tabela[0]}.csv', index=False)
    blob = bucket.blob(f'tabelas/{tabela[0]}.csv')
    blob.upload_from_filename(f'tabelas/{tabela[0]}.csv')
Conceder Acesso ao Projeto
Acesse o IAM no Google Cloud e conceda acesso ao e-mail douglas.ribeiro@soulcode.com .
Entregar o Link do Colab
Publique o link do seu caderno no Google Classroom.


[Screen recording 2024-10-31 22.30.24.webm](https://github.com/user-attachments/assets/0aa0c285-3288-4591-836a-fa6857b38c60)


[Screen recording 2024-11-01 09.58.56.webm](https://github.com/user-attachments/assets/4c6ee956-3c58-4353-a445-9a0379e9f21f)