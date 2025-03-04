# -*- coding: utf-8 -*-
"""Gabarito Exercícios Mongo Básico

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wx0qqhxN-e0QpL3V4CpduxrtQXd5uBXe
"""

import pandas as pd

!pip install pymongo

from pymongo import MongoClient

!curl ipecho.net/plain

fornecedor = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRvp1cZrRBs8Pkn45x43QITG4VdBmaHIACf1hoA9JVGOAn-VPK_YQpV7X9X4qMJldbBE9RDxoNEXAUu/pub?gid=1370589180&single=true&output=csv')
fornecedor.info()

recebimento = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRlWoWQQKZ6jY1WlP3wsORM2_TK4r7x10RZIzhDbaFHuM1-v4nQtrhtM6NPCJNqXrkM1rJzC1XWQU49/pub?gid=887958935&single=true&output=csv')
recebimento.info()

cliente = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQz4t99vzQbPSO5bMuYYos2yUxjiJAittk1DbUF6dfjh9SQPvOqsAsK0vzSde163WlhvP9sSpy9jWZr/pub?gid=1762561321&single=true&output=csv')
cliente.info()

pagamento = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSgimtgaXu_Az4aca3Uk9xXHPZx-isUbWVyijtm5Tg_NXZkuI3xgShdyz9KHqLQ2S9O0-smLS1qKN5i/pub?gid=985843317&single=true&output=csv')
pagamento.info()

banco = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSXpstJo_b9Trdg8iZhR388qnMRl1DcFkA131LcxePjSEPOzfjjNwg6NBu-yZ_Ji1KDbU8WtetPTFGl/pub?gid=1688656687&single=true&output=csv')
banco.info()

# Conectar ao MongoDB Atlas
client = MongoClient('mongodb+srv://douglasdealmeidaribeiro:c2ygnygvNLpGtOZr@cluster0.xu3hl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['financeiro']  # Nome do banco de dados

fornecedor = fornecedor.to_dict(orient='records') # transforma o df pandas em um dicionário python
db.fornecedor.insert_many(fornecedor)

recebimento = recebimento.to_dict(orient='records')
db.recebimento.insert_many(recebimento)

cliente = cliente.to_dict(orient='records')
db.cliente.insert_many(cliente)

pagamento = pagamento.to_dict(orient='records')
db.pagamento.insert_many(pagamento)

banco = banco.to_dict(orient='records')
db.banco.insert_many(banco)

'''
1 - Filtre os clientes de São Paulo e os exiba em um df pandas
'''
a = list(db.cliente.find({'Municipio':'SAO PAULO'}))
df = pd.DataFrame(a)
df.drop('_id',axis=1,inplace=True)
df.head()

'''
1 - Filtre os clientes de São Paulo e os exiba em um df pandas
'''
a = list(db.cliente.find({'UF':'SÃO PAULO'}))
df = pd.DataFrame(a)
df.drop('_id',axis=1,inplace=True)
df.head()

'''
2 - Faça uma consulta que retorne todos os fornecedores do tipo pessoa física
exiba em um df pandas
'''
fornecedores = list(db.fornecedor.find({'Tipo Pessoa':'Pessoa Física'}))
df = pd.DataFrame(fornecedores)
df.drop('_id',axis=1,inplace=True)
df.head()

'''
3 - Faça uma consulta que retorne todos os recebimentos e os exiba em um
df pandas
'''
recebimentos = list(db.recebimento.find())
df = pd.DataFrame(recebimentos)
df.drop('_id',axis=1,inplace=True)
df.head()

'''
4 - Faça uma consulta que retorne todos os pagamentos e os exiba em um
df pandas
'''
pagamentos = list(db.pagamento.find())
df = pd.DataFrame(pagamentos)
df.drop('_id',axis=1,inplace=True)
df.head()