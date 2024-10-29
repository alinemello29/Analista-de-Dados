📊 README do Projeto de Manipulação de Dados no Google Cloud Platform ☁️


🌟 Visão Geral
Este projeto visa manipular dados de um arquivo CSV obtido a partir de uma planilha Google, utilizando os recursos do Google Cloud Platform (GCP). Através de uma série de etapas, os dados serão organizados e tratados para facilitar a análise posterior. Vamos transformar dados brutos em informações valiosas! 🚀

🛠️ Requisitos do Projeto


📋 Passo a Passo
🔑 Configuração do Acesso no GCP:
Acesse seu projeto no Google Cloud Platform.
No menu IAM e Administrador, conceda acesso ao e-mail: douglas.ribeiro@soulcode.com.

🗂️ Criação do Bucket:
Crie um bucket no Google Cloud Storage onde os dados serão armazenados.

📁 Organização do Bucket:
Dentro do bucket, crie duas pastas:
dados-brutos: para armazenar os dados originais. 📥
dados-tratados: para armazenar os dados processados. 📤

📥 Download do Arquivo CSV:
Baixe o arquivo específico da Google Planilhas no formato CSV:
🔗 https://docs.google.com/spreadsheets/d/1oTKRjvTyEcScUvWqi-Arcp8AqXNeKK2iU5D4rW25cdo/edit?usp=sharing


⬆️ Upload do Arquivo:
Suba o arquivo CSV da sua máquina local para a pasta dados-brutos no bucket.
Conceda acesso público a este arquivo para permitir a leitura posterior. 🌍


📖 Leitura do Arquivo no Google Colab:
Utilize o link de acesso público do arquivo para lê-lo no Google Colab com a biblioteca pandas.


🔄 Transformação dos Dados:
Transforme cada coluna do arquivo em uma lista Python.
Utilize métodos e funções de listas aprendidos em aula para tratar os dados.


🚮 Tratamento de Dados:
Exclua registros que não tiverem todas as informações, utilizando os métodos de listas.


💾 Devolução e Salvamento:
Devolva as listas tratadas ao DataFrame do pandas.
Salve o DataFrame e envie-o automaticamente para a pasta dados-tratados do bucket na GCP.


[Screen recording 2024-10-29 11.07.49.webm](https://github.com/user-attachments/assets/d049df5d-6500-49fa-9b52-81e8c346806e)


[Screen recording 2024-10-29 11.09.07.webm](https://github.com/user-attachments/assets/4f18f36b-6072-4029-a369-f424fdd6385d)


![Screenshot 2024-10-29 11 09 57](https://github.com/user-attachments/assets/157f3196-efd7-42af-a4c2-b1fadaa4e16c)


[Screen recording 2024-10-29 11.11.22.webm](https://github.com/user-attachments/assets/f22db71c-b820-4f7b-b56a-9d5ea3754911)