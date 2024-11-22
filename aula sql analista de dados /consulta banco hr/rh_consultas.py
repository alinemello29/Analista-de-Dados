# -*- coding: utf-8 -*-
"""RH consultas

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QtfNQoMV3QC583SVYsAz_K-bu1ztMVpF
"""

!pip install mysql-connector-python

import mysql.connector
import pandas as pd

host = '34.69.233.123'
user = ''
password =''
database = 'rh'

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

consulta('''
show tables;
''','tabelas')

"""#SELECT"""

'''
Esta cláusula serve para selecionar um ou mais atributos (colunas)
de uma ou mais tabelas

Exemplo: selecionar os registros para o atributo nome da tabela
funcionarios
'''
consulta('''
SELECT nome
FROM funcionario;
''','nomes_funcionario')

'''
Exemplo: selecionar os registros para o atributo matricula e o atributo nome
da tabela funcionarios
'''
consulta('''
SELECT matricula, nome
FROM funcionario;
''','ids_nomes_funcionario')

'''
Exemplo: selecionar os registros para todos os atributos da tabela
funcionarios
'''
consulta('''
SELECT *
FROM funcionario;
''','funcionario')

"""#WHERE"""

'''
Faça uma consulta que retorne todos os nomes e cidades de clientes
que moram em Atibaia
'''
consulta('''
SELECT nome, cidade
FROM funcionario
WHERE cidade = 'Atibaia';
''','cidades')

'''
Faça uma consulta que retorne todos os nomes de funcionarios cuja nota
seja maior que 6
'''
consulta('''
SELECT nome
FROM funcionario
WHERE nota > 6;
''','aprovados')

"""#DISTINCT"""

'''
Quais são os estados (UFs) diferentes estão representados em
Nossa tabela Clientes
'''
consulta('''
SELECT DISTINCT estado
FROM funcionario
''','ufs')

"""#LIMIT"""

'''
Imagine que você deseja fazer uma consulta que retorne apenas
os cinco primeiros nomes de funcionarios
'''
consulta('''
SELECT nome
FROM funcionario
LIMIT 5;
''','primeiros_funcionario')

"""#Consultas com BOOLEANOS (E | OU | NÃO)"""

'''
Faça uma consultas que retorne todos os funcionarios que moram no estado de SP
e possuem salário acima de R$ 30.000,00
'''
consulta('''
SELECT nome, estado
FROM funcionario
WHERE estado = 'SP'
AND
salario > 30000;
''','burgueses')

'''
Faça uma consulta que retorne todos os nomes e endereços de funcionarios
que moram em SP ou MG
'''
consulta('''
SELECT nome, estado
From funcionario
WHERE estado = 'SP'
OR
estado = 'MG'
;
''','cafe_leite')

'''
Faça uma consulta que retorne todos os clientes que não sejam de SP
'''
consulta('''
SELECT nome, estado
FROM funcionario
WHERE NOT estado = 'SP';
''','no_sp')

"""#Funções de Agregação (MIN, MAX, COUNT, ROUND, AVG, SUM)

#COUNT
"""

'''
Faça uma consulta que retorne a contagem de funcionarios
'''
consulta('''
SELECT count(matricula) as Contagem
FROM funcionario;
''','contagem')

"""#AVG"""

'''
Faça uma consulta que retorne a média dos sallários
dos funcionários
'''
consulta('''
SELECT AVG(salario) salario_medio
FROM funcionario;
''','salario_medio')

"""#MAX"""

'''
Faça uma consulta que retorne o maior salário
'''
consulta('''
SELECT MAX(salario) salario_maximo
FROM funcionario;
''','maior_salario')

"""#MIN"""

'''
Faça uma consulta que retorne o menor salário
'''
consulta('''
SELECT MIN(salario) salario_minimo
FROM funcionario;
''','menor_salario')

"""#ROUND"""

'''
Faça uma consulta que retorne a média dos salaérios
 arredondada com duas casas decimais
'''
consulta('''
SELECT ROUND(AVG(salario),2) salario_medio_2
FROM funcionario;
''','salario_medio')

"""#SUM"""

'''
Faça uma consulta que retorne a soma de todas os salarios
da tabela funcionarios
'''
consulta('''
SELECT SUM(salario) as salario_total
FROM funcionario;
''','salario_total')

"""#GROUP BY"""

'''
Faça uma consulta que retorne o salário médio agrupado por
Departamento
'''
consulta('''
SELECT departamento, AVG(salario) salario_medio
FROM funcionario
GROUP BY departamento;
''','salario_departamento')

'''
Faça uma consulta que retorne a nota média por cargo
'''
consulta('''
SELECT cargo, AVG(nota) nota_media
FROM funcionario
GROUP BY cargo;
''', 'nota_por_cargo')

'''
Faça uma consulta que retorne o maior salário por cidade
'''
consulta('''
SELECT cidade, MAX(salario) as maior_salario
FROM funcionario
GROUP BY cidade;
''','maior_salario')

'''
Faça uma consulta que retorne o salário médio por departamento e cargo
'''
consulta('''
SELECT departamento, cargo, AVG(salario) salario_medio
FROM funcionario
GROUP BY departamento, cargo;
''','salario2')

"""#HAVING"""

'''
Imagine que você deseja filtrar apenas os salários médios por cidades acima de
R$ 20.000,00
'''
consulta('''
SELECT cidade, AVG(salario) as salario_medio
FROM funcionario
GROUP BY cidade
HAVING AVG(salario) > 20000;
''','medio_salario')

'''
Faça uma consulta que retorne todos os nomes de funcionarios cuja nota
seja maior que 6
'''
'''
A Cláusula HAVING substitui o WHERE quando os dados estão agrupados e agregados
'''
consulta('''
SELECT departamento, cargo, AVG(nota) nota_media
FROM funcionario
GROUP BY departamento, cargo
HAVING AVG(nota) > 6;
''','aprovados')

"""#UNION"""

'''
Imagine que você deseja criar uma consulta que retorne nome e cidade
apenas dos funcionários de Atibaia
'''
consulta('''
SELECT nome, cidade
FROM funcionario
WHERE cidade = 'Atibaia';
''','atibaia')

'''
Imagine que você deseja criar uma consulta que retorne nome e cidade
apenas dos funcionários de Extrema
'''
consulta('''
SELECT nome, cidade
FROM funcionario
WHERE cidade = 'Extrema';
''','extrema')

'''
Imagine que você deseja criar as duas consultas anteriores unidas em
uma única consulta sem usar o operador OR
'''
consulta('''
SELECT nome, cidade
FROM funcionario
WHERE cidade = 'Atibaia'
UNION
SELECT nome, cidade
FROM funcionario
WHERE cidade = 'Extrema';
''','atibaia_extrema')

"""#IN"""

'''
Imagine que você deseja fazer uma consulta que retorne os nomes e salários dos
funcionários de matrícula 1, 4 e 8
'''
consulta('''
SELECT nome, salario
FROM funcionario
WHERE matricula IN (1,4,8);
''','burguesia')

"""#BETWEEN"""

'''
Imagine que você deseja selecionar matricula e nome dos
funcionários cujas matriculas esteja entre 3 e 8
'''
consulta('''
SELECT matricula, nome
FROM funcionario
WHERE matricula BETWEEN 3 AND 8;
''','galera')

'''
Imagine que você deseja fazer uma consulta que retorne todos os nomes
de funcionários ordenados de forma crescente
'''
consulta('''
SELECT nome
FROM funcionario
ORDER BY nome ASC;
''','TOC')

'''
Imagine que você deseja fazer uma consulta que retorne todos os nomes
de funcionários ordenados de forma decrescente
'''
consulta('''
SELECT nome
FROM funcionario
ORDER BY nome DESC;
''','TOC2')

consulta('''
SELECT DEFAULT_COLLATION_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = 'rh';
''',
'''
collation
''')

'''
faça uma consulta que retorne todos os registros  com escolaridade superior
'''
consulta('''
SELECT escolaridade
FROM funcionario
WHERE escolaridade = 'superior'
''',
'''
escola
''')

'''
faça uma consulta que retorne todos os registros  com escolaridade superior
'''
consulta('''
SELECT escolaridade
FROM funcionario
WHERE BINARY escolaridade = 'superior'
''',
'''
escola
''')

"""# LIKE"""

'''
Faça uma consulta de todos os nomes de funcionários que começa a letra D
'''
consulta('''
SELECT nome
FROM funcionario
WHERE nome LIKE 'D%';
''',
'''
nomes_legais
''')

'''
Faça uma consulta que retorne todos os nomes que terminam com letra S
'''

consulta('''
SELECT nome
FROM funcionario
WHERE BINARY nome LIKE '%s';
''',
'''
nomes_legais2
''')

'''
Faça uma ocnsulta de todos os nomes que contenham
OU
'''
consulta('''
SELECT nome
FROM funcionario
WHERE BINARY nome LIKE '%ou%';
''',
'''
nomes_legais3
''')

"""#TRIM"""

'''
Faça uma consulta que retorne os nomes da cidades removendo
espaços do começo para final da string se houver
'''
consulta('''
SELECT TRIM(cidade)  as no_space
FROM funcionario;
''',''' Cidades''')

"""#REPLACE"""

'''
faça uma consulta que retorne os nomes onde a letra o seja substituida pro
dois oo
'''

consulta('''
SELECT REPLACE(nome, 'o', 'oo') as name_fun
FROM funcionario;
''',''' ''')

'''
Faça uma consulta que retorne todos os nomes em caixa alta
'''
consulta('''
SELECT UPPER(nome) mai
FROM funcionario;
''', '''mai''')

'''
Faça uma consulta que retorne todos os nomes em caixa baixa
'''
consulta('''
SELECT LOWER(nome) min
FROM funcionario;
''', '''min''')

"""
#CONCAT e CAST"""

'''
faça uam consulta que retorne a matricula ocm texto e concatenada
com o prefixo funcionario
'''
consulta('''
SELECT CONCAT('Funcionário - ', CAST(matricula AS CHAR)) matricula_texto
FROM funcionario;
''','''abc''')

"""#CASE - WHEN"""

'''
faça uma ocnsulta que retorne nome, notas e uma coluna
adiocional com aprovados para notas maiores que 6 e
provvados para os demais
'''

consulta('''
SELECT nome, nota,
  CASE WHEN nota > 6 THEN 'Aprovado'
  ELSE 'Reprovado' END
  fROM funcionario;
''', '''status''')

'''
Esse exemplos deixa mais organizado a tabela, tabela de cima foi a que prof fez
essa aqui foi um aluno que falou
'''

consulta('''
SELECT nome, nota,
  (CASE WHEN nota > 6 THEN 'Aprovado'
  ELSE 'Reprovado' END) status
  fROM funcionario;
''', '''status''')