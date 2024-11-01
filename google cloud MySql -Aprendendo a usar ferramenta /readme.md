# 🌥️ Google Cloud MySQL - Aprendendo a Usar a Ferramenta

## 📚 Sobre o Projeto
Neste projeto, aprendi a utilizar o Google Cloud MySQL para armazenar dados de um projeto desenvolvido em Python no Google Colab. Este é um passo importante para entender como integrar aplicações com bancos de dados na nuvem.


[Screen recording 2024-10-30 17.54.48.webm](https://github.com/user-attachments/assets/3b31ecc1-3f75-4f03-a288-794d83f9e061)


![Screenshot 2024-10-30 17 54 32](https://github.com/user-attachments/assets/551797cc-84b7-487a-8b34-b72906509e27)


## 🚀 Tecnologias Utilizadas
- **Google Cloud Platform** ☁️
- **MySQL** 🐬
- **Python** 🐍
- **Google Colab** 📊

## 🔧 Como Configurar
1. **Criar uma conta no Google Cloud**: Se ainda não possui, crie uma conta [aqui](https://cloud.google.com/).
2. **Criar um projeto no Google Cloud**: Siga as instruções para criar um novo projeto.
3. **Configurar o MySQL**: 
   - Ative o serviço de Cloud SQL.
   - Crie uma instância do MySQL.
   - Anote as credenciais (usuário, senha, IP).
4. **Conectar o Google Colab ao MySQL**:
   - Utilize a biblioteca `mysql-connector-python` para conectar ao banco de dados.

## 📦 Exemplo de Código
Aqui está um exemplo de como conectar ao MySQL a partir do Google Colab:

```python
import mysql.connector

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host='SEU_IP_DO_BANCO',
    user='SEU_USUARIO',
    password='SUA_SENHA',
    database='SEU_BANCO_DE_DADOS'
)

# Criação de um cursor
cursor = conn.cursor()

# Exemplo de consulta
cursor.execute("SELECT * FROM sua_tabela")

# Exibir resultados
for row in cursor.fetchall():
    print(row)

# Fechar a conexão
cursor.close()
conn.close()
🌟 Conclusão
Este projeto me ajudou a entender como funciona a integração de aplicações Python com bancos de dados na nuvem. Continue explorando e aprendendo! 🚀
