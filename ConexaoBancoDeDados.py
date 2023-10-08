
#1. Criar uma classe de conexão com o banco de dados 

import pyodbc

connstrin = "DRIVER={SQL Server};SERVER=DESKTOP-DTEG474\SQLEXPRESS;DATABASE=PythonAPIYoutube;UID=Amendoas;Trusted_Connection=yes"

#ServerName = "DESKTOP-DTEG474\SQLEXPRESS"

conexao = pyodbc.connect(connstrin)

print("Conexao com sucesso")