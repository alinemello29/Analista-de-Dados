# 📚 Aula de Pandas 🐼

Bem-vindo à aula de Pandas! Este repositório contém materiais e exemplos para aprender a usar a biblioteca Pandas em Python.

## 📖 O que é o Pandas?

Pandas é uma biblioteca poderosa e flexível que facilita a manipulação e análise de dados em Python. Com Pandas, você pode trabalhar com estruturas de dados como DataFrames e Series.

## 🛠️ Instalação

Para instalar o Pandas, você pode usar o pip:

```bash
pip install pandas
🚀 Começando
Aqui estão alguns conceitos básicos que você aprenderá:

1. Criando um DataFrame 📊
python

Copiar
import pandas as pd

dados = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(dados)
print(df)
2. Lendo e escrevendo arquivos 📂
Você pode ler e escrever arquivos CSV com facilidade:

python

Copiar
# Lendo um arquivo CSV
df = pd.read_csv('dados.csv')

# Escrevendo para um arquivo CSV
df.to_csv('saida.csv', index=False)
3. Manipulando dados 🔧
Pandas oferece várias funções para manipular dados:

Filtrar dados
Agrupar dados
Ordenar dados
python

Copiar
# Filtrando dados
df_filtrado = df[df['Idade'] > 30]
print(df_filtrado)
📚 Recursos adicionais
Documentação oficial do Pandas
Tutoriais e exemplos