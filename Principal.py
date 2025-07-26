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

    for index, row in strDataFrame.iterrows():
        posto_atendimento = Criacao_Banco.TBL_POSTO_ATENDIMENTO(CNPJ=row['Cnpj'], NOMEIF=row['NomeIf'], SEGMENTO=row['Segmento'], NOMEPOSTO=row['NomePosto'], TIPOPOSTO=row['TipoPosto'], ENDERECO=row['Endereco'], NUMERO=row['Numero'], COMPLEMENTO=row['Complemento'], BAIRRO=row['Bairro'], CEP=row['Cep'], MUNICIPIOIBGE=row['MunicipioIbge'], MUNICIPIO=row['Municipio'], UF=row['UF'], DDD=row['DDD'], TELEFONE=row['Telefone'], CNPJASSIST=row['CnpjAssist'], NOMEASSIST=row['NomeAssist'], POSICAO=row['Posicao'])
        conexao.session.add(posto_atendimento)
        conexao.session.commit()
        
        # strValores = row['Cnpj'], row['NomeIf'], row['Segmento'], row['NomePosto'], row['TipoPosto'], row['Endereco'], \
        # row['Numero'], row['Complemento'], row['Bairro'], row['Cep'], row['MunicipioIbge'], row['Municipio'], row['UF'], \
        # row['DDD'], row['Telefone'], row['CnpjAssist'], row['NomeAssist'], row['Posicao']

        # strQuery = ("INSERT INTO TBL_POSTO_ATENDIMENTO (CNPJ, NOMEIF, SEGMENTO, NOMEPOSTO,TIPOPOSTO, ENDERECO,NUMERO, COMPLEMENTO, BAIRRO, CEP, MUNICIPIOIBGE, MUNICIPIO, UF, DDD, TELEFONE, CNPJASSIST, NOMEASSIST, POSICAO) "
        #             "VALUES (%s,%s%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", strValores)
       

except Exception as Ex:
    print(Ex.args.index())
