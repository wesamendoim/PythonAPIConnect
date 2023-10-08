
#1. Criar uma classe de conexão com o banco de dados 
#2. Criar conexão com API do Youtube 
#3. Capturar os dados da API e inserir no banco de dados

#Token API Google AIzaSyDnHOCvqpzxMz8QH88yEtutIqfwMm0qHMI

import pyodbc

dados_conexao = (
    "Driver={SQL Server};" 
    "Server=DESKTOP-DTEG474;"
    "Database=PythonAPIYoutube;"
)

conexao = pyodbc.connect(dados_conexao)

print("Conexao realizada com sucesso")
