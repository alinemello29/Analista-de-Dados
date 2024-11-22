# -*- coding: utf-8 -*-
"""Exer_ter19_Criar_Banco_fazer_Consultas

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lhb7GA4tYK5pSDuF5aYhHnzjNqWUK3Qe
"""

!pip install mysql-connector-python

import mysql.connector
import pandas as pd

host = '34.69.233.123'
user = 'root'
password = ''
database = 'lanche_do_tutti'

!curl ipecho.net/plain

def consulta(query, tabela):
  connection = mysql.connector.connect(
      host = host,
      user = user,
      password = password,
      database = database
  )
  cursor = connection.cursor()

  try:
    cursor.execute(query)
    result = cursor.fetchall()
    globals()[tabela] = pd.DataFrame(result, columns=cursor.column_names)
    display(globals()[tabela])
  finally:
    cursor.close()
    connection.close()

from google.colab import files
import matplotlib.pyplot as plt
import cv2

uploaded = files.upload()

for filename in uploaded.keys():
    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image)
    plt.axis('off')
    plt.show()

consulta('''
SHOW TABLES;
''', '''df_tabelas''')

consulta('''
SELECT * FROM produtos
''', '''df_produtos''')

consulta('''
SELECT * FROM precos;
''', '''df_precos''')

consulta('''
DESCRIBE vendas;
''', ''' ''')

"""#1. Verificar a Média de Preços dos Produtos"""

consulta('''
SELECT AVG(preco) AS media_preco
FROM precos;
''', ''' ''')

"""#2. Listar Produtos com o Maior Preço"""

consulta('''
SELECT p.nome AS produto, pr.preco
FROM produtos p
JOIN precos pr ON p.id = pr.produto_id
ORDER BY pr.preco DESC
LIMIT 5;
''', ''' ''')

"""#3. Comparativo de Preços por Categoria"""

consulta('''
SELECT p.categoria, AVG(pr.preco) AS media_preco
FROM produtos p
JOIN precos pr ON p.id = pr.produto_id
GROUP BY p.categoria;
''', ''' ''')

"""# 4. Total de Vendas por Produto"""

consulta('''
SELECT p.nome AS produto, SUM(v.quantidade) AS total_vendas
FROM vendas v
JOIN produtos p ON v.produto_id = p.id
GROUP BY p.nome
ORDER BY total_vendas DESC;
''', ''' ''')

"""# 5. Total de Vendas por Data"""

consulta('''
SELECT data_venda, SUM(quantidade) AS total_vendas
FROM vendas
GROUP BY data_venda
ORDER BY data_venda;
''', ''' ''')

"""#6. Vendas de um Produto Específico"""

consulta('''
SELECT v.*
FROM vendas v
JOIN produtos p ON v.produto_id = p.id
WHERE p.nome = 'Suco';
''', ''' ''')

"""#7. Vendas Acima de um Certo Limite"""

consulta('''
SELECT *
FROM vendas
WHERE quantidade > 5;
''', ''' ''')

"""#8. Vendas por Produto"""

consulta('''
SELECT p.nome AS produto, SUM(v.quantidade) AS total_vendas
FROM vendas v
JOIN produtos p ON v.produto_id = p.id
GROUP BY p.nome
ORDER BY total_vendas DESC;
''', ''' ''')

"""#9. Vendas em um Intervalo de Datas"""

consulta('''
SELECT *
FROM vendas
WHERE data_venda BETWEEN '2023-11-01' AND '2023-11-30';
''', ''' ''')

"""#10. Vendas Mensais"""

consulta('''
SELECT DATE_FORMAT(data_venda, '%Y-%m') AS mes, SUM(quantidade) AS total_vendas
FROM vendas
GROUP BY mes
ORDER BY mes;
''', ''' ''')