# -*- coding: utf-8 -*-
"""API_Mercado_Livre

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_Qonr2lCXF9VPW9U1maLdLfdj-roo-ul
"""

import requests
import json

# Definir o termo de busca
termo_de_busca = "notebook"

# Construir a URL de requisição
url = f"https://api.mercadolibre.com/sites/MLB/search?q={termo_de_busca}"

# Fazer a requisição GET para a API
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Carregar os dados em formato JSON
    dados = response.json()

    # Exibir os dados
    print(json.dumps(dados, indent=4, ensure_ascii=False))
else:
    print(f"Erro na requisição: {response.status_code}")

# Listar as chaves principais do JSON
print("Chaves no nível superior:")
print(dados.keys())

# Explorar a chave 'results', que geralmente contém os itens principais
if 'results' in dados:
    print("\nChaves dentro de 'results':")
    if len(dados['results']) > 0:
        print(dados['results'][0].keys())
    else:
        print("Nenhum resultado encontrado em 'results'.")

"""# Resumindo o que foi visto anteriormente"""

import requests
import json
# Definir o termo de busca
termo_de_busca = "notebook"

# Construir a URL de requisição
url = f"https://api.mercadolibre.com/sites/MLB/search?q={termo_de_busca}"

# Fazer a requisição GET para a API
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Carregar os dados em formato JSON
    dados = response.json()

    # Listar as chaves principais
    print("Chaves no nível superior:")
    print(dados.keys())

    # Explorar a chave 'results' (se existir)
    if 'results' in dados:
        print("\nChaves dentro de 'results':")
        if len(dados['results']) > 0:
            print(dados['results'][0].keys())
        else:
            print("Nenhum resultado encontrado em 'results'.")
else:
    print(f"Erro na requisição: {response.status_code}")

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Carregar os dados em formato JSON
    dados = response.json()

    # Iterar sobre os resultados e extrair informações desejadas
    for item in dados.get('results', []):
        titulo = item.get('title')
        preco = item.get('price')
        link = item.get('permalink')
        print(f"Título: {titulo}\nPreço: R$ {preco}\nLink: {link}\n")
else:
    print(f"Erro na requisição: {response.status_code}")

"""# Código completo com "Pandeamento" dos dados"""

import requests
import pandas as pd

# Termo de busca
termo_de_busca = "notebook"

# URL da API do Mercado Livre
url = f"https://api.mercadolibre.com/sites/MLB/search?q={termo_de_busca}"

# Fazer a requisição GET
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Carregar os dados em formato JSON
    dados = response.json()

    # Extrair os dados relevantes
    produtos = []
    for item in dados.get('results', []):
        produto = {
            "Título": item.get('title'),
            "Preço (R$)": item.get('price'),
            "Link": item.get('permalink'),
            "Condição": item.get('condition'),
            "Categoria": item.get('category_id')
        }
        produtos.append(produto)

    # Criar o DataFrame
    df = pd.DataFrame(produtos)

    # Exibir o DataFrame
    display(df)
else:
    print(f"Erro na requisição: {response.status_code}")

df.head()

df.info()