#Arquivo principal

import ConnAPIBancoCentral
import ConexaoBancoDeDados
import Criacao_Banco
import pprint
import pandas as pd
from pandas.io import sql
import sqlalchemy as db
import pyodbc

try:
    strRetorno = ConnAPIBancoCentral.retorno_Json()
    pprint.pprint(strRetorno)
    conexao = Criacao_Banco()
    strDataFrame = pd.read_excel("strDataFrame.xlsx")

    #engine = db.create_engine( 'mssql+pyodbc://@' + server_name + '/' + database_name + '?trusted_connection=yes&driver=' + driver, fast_executemany=True)
    #strDataFrame.to_sql(con=conexao, name='TBL_POSTO_ATENDIMENTO', if_exists='replace', index=False)

    cursor = conexao.cursor()
    for index, row in strDataFrame.iterrows():

        strValores = row['Cnpj'], row['NomeIf'], row['Segmento'], row['NomePosto'], row['TipoPosto'], row['Endereco'], \
        row['Numero'], row['Complemento'], row['Bairro'], row['Cep'], row['MunicipioIbge'], row['Municipio'], row['UF'], \
        row['DDD'], row['Telefone'], row['CnpjAssist'], row['NomeAssist'], row['Posicao']

        strQuery = ("INSERT INTO TBL_POSTO_ATENDIMENTO (CNPJ, NOMEIF, SEGMENTO, NOMEPOSTO,TIPOPOSTO, ENDERECO,NUMERO, COMPLEMENTO, BAIRRO, CEP, MUNICIPIOIBGE, MUNICIPIO, UF, DDD, TELEFONE, CNPJASSIST, NOMEASSIST, POSICAO) "
                    "VALUES (%s,%s%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", strValores)

        cursor.execute(strQuery)
        cursor.commit()


except Exception as Ex:
    print(Ex.args.index())
