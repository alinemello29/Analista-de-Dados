# -*- coding: utf-8 -*-
"""Fear of The PySpark

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q28kwrNbdVTRCKEqmhL7x19PHNoQ-pnw
"""

# Importação da biblioteca pandas
import pandas as pd

# Instalação dos requisitos para o PySpark
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q http://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz
!tar xf spark-3.1.1-bin-hadoop3.2.tgz
!pip install -q findspark

# Configurar as variáveis de ambiente
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.1.1-bin-hadoop3.2"
# Torna o pyspark "importável"
import findspark
findspark.init()

from pyspark.sql import SparkSession

# Inicializar a SparkSession com suporte ao Hive
spark = SparkSession.builder \
    .appName("Spark with Hive on Colab") \
    .config("spark.sql.catalogImplementation", "hive") \
    .config("spark.sql.warehouse.dir", "/content/spark-warehouse") \
    .config("hive.metastore.warehouse.dir", "/content/spark-warehouse") \
    .enableHiveSupport() \
    .getOrCreate()

# Criar diretório para o warehouse
!mkdir -p /content/spark-warehouse

# Verifica o SparkContext
print(spark)

# Exibe a Spark version
print(spark.version)

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vR2snMwL0lRHwNv3ilck0T98nhhyAqzmU5oQMKY4nwKZu_0FkiGo8U7ZXvA63CQOg2bYfmhKc6c-dL1/pub?gid=0&single=true&output=csv')
display(df)

df.to_csv('dados.csv',index=False)

df.info()

display(df)

for i in range(df.shape[0]):
  print(tuple(df.iloc[i]))

"""# Criando um DF PySpark"""

# Cria a tabela funcionários
spark.sql('''
CREATE TABLE IF NOT EXISTS funcionarios (
  matricula INT,
  nome STRING,
  cidade STRING,
  estado STRING,
  pais STRING,
  idade INT,
  departamento STRING,
  cargo STRING,
  salario DOUBLE,
  escolaridade STRING,
  nota INT
)
''')

# Populando a tabela funcionarios
spark.sql('''
INSERT INTO funcionarios VALUES
(1, 'Lucas', 'Atibaia', 'SP', 'Brasil', 35, 'Compras', 'Gerente', 25000, 'Superior', 8),
(2, 'Ana', 'São Paulo', 'SP', 'Brasil', 29, 'Vendas', 'Coordenador', 12000, 'Superior', 6),
(3, 'Luiza', 'Santos', 'SP', 'Brasil', 38, 'Finanças', 'Gerente', 28000, 'MBA', 9),
(4, 'Fernando', 'Atibaia', 'SP', 'Brasil', 36, 'Marketing', 'Diretor', 40000, 'Mestrado', 7),
(5, 'Sandra', 'Atibaia', 'SP', 'Brasil', 28, 'Produção', 'Analista', 23000, 'Superior', 5),
(6, 'Douglas', 'Bragança', 'SP', 'Brasil', 29, 'Finanças', 'Analista', 11000, 'Superior', 9),
(7, 'Eduardo', 'Extrema', 'MG', 'Brasil', 30, 'Marketing', 'Gerente', 12000, 'MBA', 4),
(8, 'Ester', 'Itapeva', 'MG', 'Brasil', 29, 'Compras', 'Analista', 10000, 'Superior', 2),
(9, 'Pedro', 'Extrema', 'MG', 'Brasil', 30, 'Marketing', 'Analista', 13000, 'Superior', 1),
(10, 'Maria', 'Extrema', 'MG', 'Brasil', 40, 'Produção', 'Analista', 12000, 'MBA', 7)
''')

funcionarios = spark.sql('''
SELECT *
FROM funcionarios
''')

funcionarios.show()

# Transformando o objeto funcionarios em um df pandas
df = funcionarios.toPandas()
display(df)

# Convertendo um ojeto pandas em um df pyspark
dfpy = spark.createDataFrame(df.to_dict(orient='records'))

# Exibindo os result
dfpy.show()

# Cria a tabela funcionários2
spark.sql('''
CREATE TABLE IF NOT EXISTS funcionarios2 (
  matricula INT,
  nome STRING,
  cidade STRING,
  estado STRING,
  pais STRING,
  idade INT,
  departamento STRING,
  cargo STRING,
  salario DOUBLE,
  escolaridade STRING,
  nota INT
)

USING CSV
OPTIONS (path '/content/dados.csv', header 'true', inferSchema 'true')
''')
spark.sql('''
SELECT *
FROM funcionarios2
''').show()

'''
Crie uma visão do salário médio agrupado por cargo
'''
df[['cargo','salario']].groupby('cargo').mean().reset_index()

'''
Crie uma visão do salário médio agrupado por cargo
'''
spark.sql('''
SELECT cargo, ROUND(AVG(salario),1) AS salario_medio
FROM funcionarios
GROUP BY cargo
''').show()

'''
Vamor fazer uma consulta que retorne apenas os nomes e salários,
cujo salário seja maior que 20.000
'''
df.loc[df['salario'] > 20000,['nome','salario']]

'''
Vamor fazer uma consulta que retorne apenas os nomes e salários,
cujo salário seja maior que 20.000
'''
spark.sql('''
SELECT nome, salario
FROM funcionarios
WHERE salario > 20000
''').show()

"""# Banco querida locadora"""

cliente = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQW3fP3j4qoiMGBXDAGzg_9IW2b3zgjdkVKLsURNVe9QezpHXimWfKle_55CQQtkeWL69OAASBDNdk8/pub?gid=2073489257&single=true&output=csv')
display(cliente)

aluguel = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRncyLGO1iOo2H53JaryzVF1GPjUhWl9DsN7TZROCDxaP85iCwl5aW5ffBEzqtpAMRNYkd7eO5ehmgn/pub?gid=1581881382&single=true&output=csv')
display(aluguel)

carro = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSznlX7UXeH_LeKcNteiDnWvdwZyydAQl0_x8NU9cx6G00Zh7SMrjoUuNpytVq7U-iQVzQNJ7jC7GpY/pub?gid=306989914&single=true&output=csv')
display(carro)

marca = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSI-4_QEFwZ6eDGwUDlip0_PGBn7d_F7j59UwXmRvWbQFyy01ENPatjkbO1E8k5ZW5lqSY9ox112j7X/pub?gid=1160143272&single=true&output=csv')
display(marca)

cliente.to_csv('cliente.csv',index=False)

aluguel.to_csv('aluguel.csv',index=False)

marca.to_csv('marca.csv',index=False)

carro.to_csv('carro.csv',index=False)

cliente.info()

# Cria a tabela cliente
spark.sql('''
CREATE TABLE IF NOT EXISTS cliente (
  codcliente INT,
  nome STRING,
  cidade STRING,
  sexo STRING,
  estado STRING,
  estadocivil STRING
)

USING CSV
OPTIONS (path '/content/cliente.csv', header 'true', inferSchema 'true')
''')
cliente = spark.sql('''
SELECT *
FROM cliente
''')

cliente.show()

aluguel.info()

# Cria a tabela aluguel
spark.sql('''
CREATE TABLE IF NOT EXISTS aluguel (
  codaluguel INT,
  codcliente INT,
  codcarro INT,
  data_aluguel DATE
)

USING CSV
OPTIONS (path '/content/aluguel.csv', header 'true', inferSchema 'true')
''')
aluguel = spark.sql('''
SELECT *
FROM aluguel
''')

aluguel.show()

carro.info()

# Cria a tabela carro
spark.sql('''
CREATE TABLE IF NOT EXISTS carro (
  codcarro INT,
  codmarca INT,
  modelo STRING,
  valor DOUBLE
)

USING CSV
OPTIONS (path '/content/carro.csv', header 'true', inferSchema 'true')
''')
carro = spark.sql('''
SELECT *
FROM carro
''')

carro.show()

marca.info()

# Cria a tabela marca
spark.sql('''
CREATE TABLE IF NOT EXISTS marca (
  codmarca INT,
  marca STRING
)

USING CSV
OPTIONS (path '/content/marca.csv', header 'true', inferSchema 'true')
''')
marca = spark.sql('''
SELECT *
FROM marca
''')

marca.show()

'''
1 - Selecione todos os dados da tabela cliente
'''
spark.sql('''
SELECT *
FROM cliente
''').show()

'''
2 - Liste os estados diferentes presentes na tabela cliente.
'''
spark.sql('''
SELECT DISTINCT estado
FROM cliente
''').show()

'''
3 - Encontre todos os clientes que são do sexo feminino e solteiros.
'''
spark.sql('''
SELECT nome, sexo, estadocivil
FROM cliente
WHERE sexo = "F"  AND estadocivil = "S"
''').show()

'''
4 - Liste todos os clientes cujo nome começa com a letra 'A'.
'''
spark.sql('''
SELECT *
FROM cliente
WHERE nome LIKE "A%"
''').show()

'''
5 - Liste todos os carros que são da marca 'Ford' ou 'Fiat'.
'''
spark.sql('''
SELECT carro.modelo, marca.marca
FROM carro
JOIN marca
ON carro.codmarca = marca.codmarca
WHERE marca.marca = "Fiat" OR marca.marca = "Ford"
''').show()

'''
6 - Encontre os clientes que alugaram o carro com modelo 'Onix'.
'''
spark.sql('''
SELECT cliente.nome, carro.modelo
FROM aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro
WHERE modelo = "Onix"
''').show()

'''
7 - Liste os modelos de carros e o número de vezes que cada um foi alugado.
'''
spark.sql('''
SELECT carro.modelo, COUNT(codaluguel) AS qtde_alugueis
FROM aluguel
JOIN carro ON aluguel.codcarro = carro.codcarro
GROUP BY modelo
ORDER BY COUNT(codaluguel) DESC
''').show()

'''
8 - Liste o nome dos clientes e o número de aluguéis que cada um fez.
'''
spark.sql('''
SELECT cliente.nome, COUNT(codaluguel) AS qtde_alugueis
FROM aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
GROUP BY nome
ORDER BY COUNT(codaluguel) DESC
''').show()

'''
9 - Crie uma consulta que retorne o nome dos clientes e uma coluna adicional
chamada status_civil que classifica os clientes como "Solteiro" ou "Casado".
'''
spark.sql('''
SELECT nome, CASE WHEN estadocivil = "S" THEN "Solteiro" WHEN estadocivil =
"C" THEN "Casado" END AS status_civil
FROM cliente
''').show()

'''
10 - Encontre os clientes que alugaram carros em um determinado mês e ano,
listando os modelos de carros e as datas de aluguel.
'''
spark.sql('''
SELECT cliente.nome,
       carro.modelo,
       aluguel.data_aluguel
FROM aluguel
JOIN cliente ON aluguel.codcliente = cliente.codcliente
JOIN carro ON aluguel.codcarro = carro.codcarro
WHERE
MONTH(aluguel.data_aluguel) = 4 AND YEAR(aluguel.data_aluguel) = 2023
''').show()

aluguel.show()