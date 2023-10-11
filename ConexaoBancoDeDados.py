import pprint

#1. Criar uma classe de conexão com o banco de dados
#ServerName = "DESKTOP-DTEG474\SQLEXPRESS"
global conexao
global cursor
import pyodbc
import mysql.connector
import pandas

def conexaoBanco(*args):

    try:
        #connstrin = "DRIVER={SQL Server};SERVER=DESKTOP-DTEG474\SQLEXPRESS;DATABASE=PythonAPIYoutube;UID=Amendoas;Trusted_Connection=yes"
        #conexao = pyodbc.connect(connstrin)
        conexao = mysql.connector.connect(host="database-1.cgvkcxzfdedj.sa-east-1.rds.amazonaws.com", database="APIBancoCentral", user="admin", password="paramore")
        return conexao
    except Exception:
        raise Exception('Erro de conexao')
