# -*- coding: utf-8 -*-
"""DDL

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LsxYd-cXF5oUr9BIkCby-GqjTgP9Ijjn

#CRUD-CREATE-READ,UPDATE,DELETE
"""

!pip install mysql-connector-python

import mysql.connector
import pandas as pd

host = '34.69.233.123'
user = 'root'
password = ''
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

def ddl(comando):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()

    try:
        cursor.execute(comando)
        connection.commit()  # Confirma as mudanças no banco
        print(f"Comando DDL executado com sucesso:\n{comando}")
    except mysql.connector.Error as err:
        print(f"Erro ao executar o comando DDL: {err}")
    finally:
        cursor.close()
        connection.close()

consulta('SHOW TABLES', 'minha_tabela')

"""#C  do CRUD

#criacão e modificação de tabelas
"""

#criar tabela pagamento
ddl('''
CREATE TABLE pagamentos (
   codpagamento INT PRIMARY KEY,
   codaluguel INT,
   valor FLOAT,
   data_pagamento DATE,
   FOREIGN KEY (codaluguel) REFERENCES aluguel (codaluguel)
);
''')

consulta('''
SHOW TABLES;
''',''' ''')

#adocionar coluna emial em cliente
ddl('''
ALTER TABLE cliente ADD COLUMN email VARCHAR(255);
''')

consulta('''
DESC cliente;
''', ''' ''')

#aletrar tipo de coluna valor em carro
ddl('''
ALTER TABLE carro MODIFY COLUMN valor DECIMAL(10, 2)
''')

consulta('''
DESC carro;
''', ''' ''')

#renomaer coluna estado para uf em clinte
ddl('''
ALTER TABLE cliente CHANGE COLUMN estado uf CHAR(2);
''')

consulta('''
DESC cliente;
''', ''' ''')

#adicionar NOT NULL na colunama marca em marca
ddl('''
ALTER TABLE marca MODIFY COLUMN marca VARCHAR(255) NOT NULL;
''')

consulta('''
DESCRIBE marca;
''', ''' ''')

#remover colun estadocivil em cliente
ddl('''
ALTER TABLE cliente DROP COLUMN estadocivil;
''')

consulta('''
DESCRIBE cliente;
''', ''' ''')

#excluir tabela pagamentos
ddl('''
DROP TABLE pagamentos;
''')

#remover coluna daat_aluguel em aluguel
ddl('''
ALTER TABLE aluguel DROP COLUMN data_aluguel;
''')

#DELETAR banco locadora
ddl('''
DROP DATABASE locadora;
''')

"""#Reconstruindo o banc lacoradora"""

ddl('''
CREATE TABLE cliente(
codcliente INT PRIMARY KEY,
nome VARCHAR(50),
cidade VARCHAR(50),
sexo CHAR(1),
estado CHAR(2),
estadocivil CHAR(1)
);
''')

ddl('''
CREATE TABLE marca(
codmarca INT PRIMARY KEY,
marca VARCHAR(30)
);
''')

ddl('''
CREATE TABLE carro(
codcarro INT PRIMARY KEY,
codmarca INT,
modelo VARCHAR(30) NOT NULL,
valor FLOAT,
FOREIGN KEY (codmarca) REFERENCES marca (codmarca)
);
''')

ddl('''
CREATE TABLE aluguel(
codaluguel INT PRIMARY KEY,
codcliente INT,
codcarro INT,
data_aluguel DATE,
FOREIGN KEY (codcliente) REFERENCES cliente (codcliente),
FOREIGN KEY (codcarro) REFERENCES carro (codcarro)
);
''')

ddl('''
INSERT INTO cliente (codcliente, nome, cidade, sexo, estado, estadocivil)
VALUES
(1, 'Ana Silva', 'Duque de Caxias', 'F', 'RJ', 'C'),
(2, 'Bruna Pereira', 'Niterói', 'F', 'RJ', 'C'),
(3, 'Túlio Nascimento', 'Duque de Caxias', 'M', 'RJ', 'S'),
(4, 'Fernando Souza', 'Campinas', 'M', 'SP', 'S'),
(5, 'Lúcia Andrade', 'São Paulo', 'F', 'SP', 'C');
''')

ddl('''
INSERT INTO marca (codmarca, marca) VALUES
(1, 'Ford'),
(2, 'Fiat'),
(3, 'Chevrolet'),
(4, 'Volkswagen'),
(5, 'Renault');
''')

ddl('''
INSERT INTO carro (codcarro, modelo, codmarca, valor) VALUES
(1, 'Ka', 1, 100.00),
(2, 'Argo', 2, 150.00),
(3, 'Onix', 3, 170.00),
(4, 'Polo', 4, 150.00),
(5, 'Kwid', 5, 120.00);
''')

ddl('''
INSERT INTO aluguel (codaluguel, codcliente, codcarro, data_aluguel)VALUES
(1, 3, 2, '2023-04-01'),
(2, 2, 1, '2023-04-02'),
(3, 2, 1, '2023-04-03'),
(4, 2, 3, '2023-04-04'),
(5, 1, 4, '2023-04-05'),
(6, 1, 4, '2023-04-13'),
(7, 1, 1, '2023-04-15'),
(8, 5, 2, '2023-04-19'),
(9, 5, 2, '2023-04-21'),
(10,3, 1, '2023-04-25');
''')

#inserir cliente "João Silva"
ddl('''
INSERT INTO cliente (codcliente, nome, cidade, estado, estadocivil)
VALUES (6, 'João Silva', 'São Paulo', 'SP', 'S');
''')

#inserir marca "Toyota"
ddl('''
INSERT INTO marca (codmarca, marca)
VALUES (6, 'toyota');
''')

#inserir aluguel para cliente 1  e carro 2 na data atual
ddl('''
INSERT INTO aluguel (codaluguel, codcliente, codcarro, data_aluguel)
VALUES (11, 1, 2, CURDATE());
''')

#inserir marca "mercedes"
ddl('''
INSERT INTO marca (codmarca, marca)
VALUE (7, 'Mercedes');
''')

consulta('''
select * from aluguel;
''', ''' ''')

"""#Upadate"""

1# Atualizar nome do cliente 1

ddl('''
UPDATE cliente
SET nome = 'Aline Melo' #nome era ana silava coloquei alin melo
WHERE codcliente = 1; # se não coloca where todos os nome iria er aline melo
''')

consulta('''
select * from cliente;
''', ''' ''')

ddl('''
UPDATE carro
SET valor = 200
WHERE codcarro = 3;
''')

consulta('''
select *from carro;
''', ''' ''')

#deletar kwid da base
ddl('''
DELETE FROM carro
WHERE modelo = 'kwid';
''')

consulta('''
select * from carro;
''', ''' ''')

#deletar clinete 5
consulta ('''
select * from cliente;
''', ''' ''')

#deletar o clinte 5 da base de aluguel
ddl('''
DELETE FROM aluguel
WHERE codcliente = '5'
''')

#deletar o clinte 5 da base de cliente
ddl('''
DELETE FROM cliente
WHERE codcliente = '5'
''')

#remover clinete com estados civil '
ddl('''
DELETE FROM cliente
WHERE codcliente =  4;
''')