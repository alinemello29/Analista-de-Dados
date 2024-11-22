# -*- coding: utf-8 -*-
"""50_Exer_SQL_Locadora

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/108COIHa_YEfJsVjmLU28wmONq3nuEW5K
"""

!pip install mysql-connector-python

import mysql.connector
import pandas as pd

host = '34.69.233.123'
user = ''
password =''
database = 'locadora'

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

"""#1 - Selecione todos os dados da tabela cliente"""

consulta('''
SELECT * FROM cliente;
''', ''' ''')

"""#2 - Liste todos os clientes que moram na cidade de "São Paulo"."""

consulta('''
SELECT * FROM cliente
WHERE cidade = 'São Paulo';
''', ''' ''')

"""#3 - Liste os estados diferentes presentes na tabela cliente."""

consulta('''
SELECT DISTINCT estado FROM cliente;
''', ''' ''')

"""#4 - Liste todos os clientes ordenados pelo nome em ordem alfabética."""

consulta('''
SELECT * FROM cliente
ORDER BY nome ASC;
''',''' ''')

"""# 5. Encontre todos os clientes que são do sexo feminino e solteiros."""

consulta('''
SELECT * FROM cliente
WHERE sexo = 'Feminino' AND estadocivil = 'Solteiro';
''', ''' ''')

"""# 6. Liste todos os clientes cujo nome começa com a letra 'A'."""

consulta('''
SELECT * FROM cliente WHERE nome LIKE 'A%';
''', ''' ''')

"""# 7. Selecione os 3 primeiros registros da tabela cliente."""

consulta('''
SELECT * FROM cliente LIMIT 3;
''', ''' ''')

"""# 8. Liste todos os carros que são da marca 'Ford' ou 'Fiat'."""

consulta('''
SELECT * FROM carro
WHERE modelo IN ('Ford');
''', ''' ''')

"""# 9. Encontre todos os carros cujo valor está entre 100 e 150."""

consulta('''
SELECT * FROM carro WHERE valor BETWEEN 100 AND 150;
''', ''' ''')

"""# 10. Conte quantos aluguéis foram realizados."""

consulta('''
SELECT COUNT(*) FROM aluguel;
''', ''' ''')

"""# 11. Calcule o valor total de todos os carros disponíveis para aluguel."""

consulta('''
SELECT SUM(valor) FROM carro;
''', 'valor total de todos os carros')

"""# 12. Calcule o valor médio dos carros."""

consulta('''
SELECT AVG(valor) FROM carro;
''', ''' ''')

"""# 13. Encontre o menor e o maior valor de aluguel de carros."""

consulta('''
SELECT MIN(valor) AS menor_valor, MAX(valor) AS maior_valor FROM carro;
''', ''' ''')

"""# 14. Agrupe os clientes por estado e conte quantos clientes existem em cada estado."""

consulta('''
SELECT estado, COUNT(*) FROM cliente GROUP BY estado;
''', ''' ''')

"""# 15. Agrupe os aluguéis por cliente e filtre apenas aqueles que fizeram mais de 2 aluguéis."""

consulta('''
SELECT codcliente, COUNT(*)
FROM aluguel
GROUP BY codcliente
HAVING COUNT(*) > 2;
''', ''' ''')

"""# 16. Liste todos os aluguéis, mostrando o nome do cliente e o modelo do carro alugado."""

consulta('''
SELECT c.nome, car.modelo
FROM aluguel a
JOIN cliente c ON a.codcliente = c.codcliente
JOIN carro car ON a.codcarro = car.codcarro;
''', ''' ''')

"""# 17. Liste todos os carros e, se houver, as informações sobre os aluguéis realizados desses carros."""

consulta('''
SELECT car.*, a.data_aluguel
FROM carro car
LEFT JOIN aluguel a ON car.codcarro = a.codcarro;
''', ''' ''')

"""# 18. Liste todos os aluguéis e as informações sobre os carros alugados, mesmo que o carro não esteja mais no banco de dados."""

consulta('''
SELECT a.*, car.modelo
FROM aluguel a
LEFT JOIN carro car ON a.codcarro = car.codcarro;
''', ''' ''')

"""# 19. Liste todos os clientes e os carros que alugaram, incluindo clientes que não alugaram e carros que não foram alugados."""

consulta('''
SELECT c.nome, car.modelo
FROM cliente c
LEFT JOIN aluguel a ON c.codcliente = a.codcliente
LEFT JOIN carro car ON a.codcarro = car.codcarro;
''', ''' ''')

"""# 20. Combine os resultados de duas consultas: uma que lista clientes solteiros e outra que lista clientes casados."""

consulta('''
SELECT * FROM cliente WHERE estado = 'Solteiro'
UNION
SELECT * FROM cliente WHERE estado = 'Casado';
''', ''' ''')

"""# 21. Encontre os clientes que alugaram o carro com modelo 'Onix'."""

consulta('''
SELECT c.*
FROM cliente c
JOIN aluguel a ON c.codcliente = a.codcliente
JOIN carro car ON a.codcarro = car.codcarro
WHERE car.modelo = 'Onix';
''', ''' ''')

"""# 22. Liste os modelos de carros e o número de vezes que cada um foi alugado."""

consulta('''
SELECT car.modelo, COUNT(a.codaluguel) AS quantidade
FROM carro car
LEFT JOIN aluguel a ON car.codcarro = a.codcarro
GROUP BY car.modelo;
''' ''', ''')

"""# 23. Liste o nome dos clientes e o número de aluguéis que cada um fez."""

consulta('''
SELECT c.nome, COUNT(a.codaluguel) AS quantidade
FROM cliente c
LEFT JOIN aluguel a ON c.codcliente = a.codcliente
GROUP BY c.nome;
''', ''' ''')

"""# 24. Crie uma consulta que retorne o nome dos clientes e uma coluna adicional chamada status_civil que classifica os clientes como "Solteiro" ou "Casado"."""

consulta('''
SELECT nome, estadocivil AS status_civil
FROM cliente;
''', ''' ''')

"""# 25. Liste os nomes dos clientes e as datas em que alugaram carros."""

consulta('''
SELECT c.nome, a.data_aluguel
FROM cliente c
JOIN aluguel a ON c.codcliente = a.codcliente;
''', ''' ''')

"""# 26. Liste todos os modelos de carros e suas respectivas marcas."""

consulta('''
SELECT modelo
marca FROM carro;
''', ''' ''')

"""# 27. Liste todos os aluguéis e os nomes dos clientes que os realizaram."""

consulta('''
SELECT a.*, c.nome
FROM aluguel a
JOIN cliente c ON a.codcliente = c.codcliente;
''', ''' ''')

"""# 28. Encontre o nome dos clientes e os modelos de carros que alugaram."""

consulta('''
SELECT c.nome, car.modelo
FROM cliente c
JOIN aluguel a ON c.codcliente = a.codcliente
JOIN carro car ON a.codcarro = car.codcarro;
''', ''' ''')

"""# 29. Liste todos os carros e, se houver, mostre as datas em que foram alugados."""

consulta('''
SELECT c.codcarro, c.codmarca, c.modelo, c.valor, a.data_aluguel
FROM carro c
LEFT JOIN aluguel a ON c.codcarro = a.codcarro;
''', ''' ''')

"""# 30. Encontre os clientes que moram na mesma cidade e estado e que alugaram carros."""

consulta('''
SELECT DISTINCT c1.nome AS cliente_1,
                c2.nome AS cliente_2,
                c1.estado,
                c1.cidade

FROM cliente c1
JOIN cliente c2 ON c1.cidade = c2.cidade AND c1.estado = c2.estado AND c1.codcliente <> c2.codcliente
JOIN aluguel a1 ON c1.codcliente = a1.codcliente
JOIN aluguel a2 ON c2.codcliente = a2.codcliente;
''',''' ''')

"""# 31. Liste os nomes dos clientes e os carros que eles alugaram, incluindo os clientes que não alugaram nenhum carro."""

consulta('''
SELECT cliente.nome, carro.modelo
FROM cliente
LEFT JOIN aluguel
ON cliente.codcliente = aluguel.codcliente
LEFT JOIN carro
ON aluguel.codcarro = carro.codcarro;
''', ''' ''')

"""# 32. Liste todas as marcas e, se houver, os modelos de carros associados."""

consulta('''
SELECT codmarca, modelo FROM carro;
''', ''' ''')

"""# 33. Encontre todos os aluguéis e o estado civil dos clientes que alugaram os carros."""

consulta('''
SELECT aluguel.codaluguel,
       cliente.nome,
       cliente.estadocivil,
       aluguel.data_aluguel
FROM aluguel
JOIN cliente
ON aluguel.codcliente = cliente.codcliente
ORDER BY aluguel.codaluguel;
''', ''' ''')

"""# 34. Liste os clientes e as cidades em que moram para aqueles que alugaram carros."""

consulta('''
SELECT DISTINCT cliente.nome,
       cliente.cidade
FROM cliente
JOIN aluguel
ON aluguel.codcliente = cliente.codcliente;
''', ''' ''')

"""# 35. Liste os clientes que alugaram carros e os modelos de carros que eles alugaram, incluindo a marca do carro."""

consulta('''
SELECT DISTINCT cliente.nome,
       carro.modelo,
       marca.marca
FROM aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro
JOIN marca ON carro.codmarca = marca.codmarca
ORDER BY cliente.nome;
''', ''' ''')

"""# 36. Encontre todos os aluguéis realizados em uma cidade específica e liste os nomes dos clientes e os modelos de carros alugados."""

consulta('''
SELECT cliente.nome,
       carro.modelo,
       cliente.cidade
FROM aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro
WHERE cliente.cidade = 'Niterói';
''', ''' ''')

"""# 37. Liste os modelos de carros e a quantidade de vezes que foram alugados."""

consulta('''
SELECT carro.modelo,
       COUNT(aluguel.codcarro) AS qtde
FROM carro
JOIN aluguel ON carro.codcarro = aluguel.codcarro
GROUP BY carro.modelo
ORDER BY COUNT(aluguel.codcarro) DESC;
''', ''' ''')

"""# 38. Encontre os clientes que alugaram mais de um carro."""

consulta('''
SELECT cliente.nome,
       COUNT(aluguel.codcarro) AS qtde_de_alugueis
FROM aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
GROUP BY
  cliente.nome
HAVING COUNT(aluguel.codcarro) > 1
ORDER BY COUNT(aluguel.codcarro) DESC;
''', ''' ''')

"""# 39. Liste os clientes, as datas de aluguel e o valor do carro alugado."""

consulta('''
SELECT cliente.nome,
       aluguel.data_aluguel,
       carro.valor
FROM aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro;
''', ''' ''')

"""# 40. Liste os modelos de carros que nunca foram alugados."""

consulta('''
SELECT carro.modelo
FROM carro
LEFT JOIN aluguel ON carro.codcarro = aluguel.codcarro
WHERE aluguel.codcarro IS NULL;
''', ''' ''')

"""# 41. Encontre os clientes que alugaram carros e o total gasto em aluguéis."""

consulta('''
SELECT cliente.nome,
       SUM(valor) AS Valor_total
FROM aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro
GROUP BY cliente.nome
ORDER BY cliente.nome;
''', ''' ''')

"""# 42. Liste as marcas de carros e o número total de aluguéis por marca."""

consulta('''
SELECT marca.marca,
       COUNT(aluguel.codaluguel) QTDE
FROM marca
JOIN carro ON marca.codmarca = carro.codmarca
JOIN aluguel ON carro.codcarro = aluguel.codcarro
GROUP BY
  marca.marca
ORDER BY COUNT(aluguel.codaluguel)  DESC;
''', ''' ''')

"""# 43. Encontre os clientes que alugaram carros em um determinado mês e ano, listando os modelos de carros e as datas de aluguel."""

consulta('''
SELECT cliente.nome,
       carro.modelo,
       aluguel.data_aluguel
FROM aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro
WHERE
MONTH(aluguel.data_aluguel) = 4 AND YEAR(aluguel.data_aluguel) = 2023;
''', ''' ''')

"""# 44. Liste os clientes que moram em estados diferentes e que alugaram carros, junto com os modelos alugados."""

consulta('''
SELECT DISTINCT cliente.nome,
                cliente.estado,
                carro.modelo
FROM cliente
JOIN aluguel
ON aluguel.codcliente = cliente.codcliente
JOIN carro
ON carro.codcarro = aluguel.codcarro
ORDER BY cliente.estado, cliente.nome;
''', ''' ''')

"""# 45. Encontre os clientes que alugaram carros, os modelos de carros alugados, as marcas desses carros e as datas de aluguel, ordenando pelos nomes dos clientes."""

consulta('''
SELECT cliente.nome,
       carro.modelo,
       marca.marca,
       aluguel.data_aluguel
FROM aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro
JOIN marca ON carro.codmarca = marca.codmarca
ORDER BY cliente.nome;
''', ''' ''')

"""# 46. Liste os clientes que alugaram carros mais de uma vez e os detalhes dos carros que alugaram."""

consulta('''
SELECT
    cliente.nome AS nome_cliente,
    carro.modelo AS modelo_carro,
    marca.marca AS nome_marca,
    aluguel.data_aluguel
FROM
    aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro
JOIN marca ON carro.codmarca = marca.codmarca
WHERE
    aluguel.codcliente IN (
        SELECT codcliente
        FROM aluguel
        GROUP BY codcliente
        HAVING COUNT(codaluguel) > 1
    )
ORDER BY
    cliente.nome;
''', ''' ''')

"""# 47. Encontre os modelos de carros que foram alugados por clientes de cidades específicas e liste as marcas desses carros."""

consulta('''
SELECT cliente.nome,
       cliente.cidade,
       carro.modelo,
       marca.marca
FROM aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro
JOIN marca ON marca.codmarca = carro.codmarca
WHERE cliente.cidade = 'Niterói'
OR cliente.cidade = 'São Paulo';
''', ''' ''')

"""# 48. Liste os clientes que alugaram carros, os modelos e as marcas dos carros, e o total gasto em aluguéis, agrupado por cliente."""

consulta('''
SELECT DISTINCT cliente.nome,
       carro.modelo,
       marca.marca,
       SUM(carro.valor)
FROM aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro
JOIN marca ON carro.codmarca = marca.codmarca
GROUP BY
    cliente.nome,
    carro.modelo,
    marca.marca;
''', ''' ''')

"""# 49. Encontre os carros que foram alugados nos últimos 30 dias e os clientes que os alugaram."""

consulta('''
SELECT
    cliente.nome AS nome_cliente,
    carro.modelo AS modelo_carro,
    aluguel.data_aluguel
FROM
    aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro
WHERE
    aluguel.data_aluguel >= DATE_SUB(CURDATE(), INTERVAL 730 DAY);;
''', ''' ''')

"""# 50. Liste os clientes, os carros que alugaram, as marcas desses carros, e o valor total gasto em aluguéis, filtrando por um intervalo de datas específico."""

consulta('''
SELECT
    cliente.nome AS nome_cliente,
    carro.modelo AS modelo_carro,
    marca.marca AS nome_marca,
    SUM(carro.valor) AS total_gasto
FROM
    aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro
JOIN marca ON carro.codmarca = marca.codmarca
WHERE
    aluguel.data_aluguel BETWEEN '2022-10-19' AND '2024-11-18'
GROUP BY
    cliente.codcliente, cliente.nome, carro.modelo, marca.marca;
''', ''' ''')