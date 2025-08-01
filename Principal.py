#Arquivo principal

import ConnAPIBancoCentral
#import ConexaoBancoDeDados
import Criacao_Banco
import pprint
import pandas as pd
from pandas.io import sql
import sqlalchemy as db
import pyodbc
import openpyxl
import Dashborad
import os

try:
    strRetorno = ConnAPIBancoCentral.retorno_Json()
    #strDataFrame = pd.read_excel("strDataFrame.xlsx")
    strRetorno_df = pd.DataFrame(strRetorno)
    pprint.pprint(strRetorno_df)
    linhasJson = strRetorno_df.to_dict(orient='records')
    print(linhasJson.append(strRetorno_df['value']))

    # Supondo que strRetorno_df já existe e tem a coluna 'value'
    tabela = pd.json_normalize(strRetorno_df['value'])

    # Agora 'tabela' é um DataFrame com cada campo do dicionário como coluna
    print(tabela.head())

    # Se quiser salvar como Excel:
    tabela.to_excel("strDataFrame.xlsx", index=False)

    strDataFrame = pd.read_excel("strDataFrame.xlsx")

    for index, row in strDataFrame.iterrows():
            #Verificar se o CNPJ já existe na tabela
            existe = Criacao_Banco.session.query(Criacao_Banco.TBL_POSTO_ATENDIMENTO).filter_by(CNPJ=row['Cnpj']).first()
            #print(existe.CNPJ)

            # Se o CNPJ não existir, insira os dados
            if not existe:
                    posto_atendimento = Criacao_Banco.TBL_POSTO_ATENDIMENTO(CNPJ=row['Cnpj'], NOMEIF=row['NomeIf'], SEGMENTO=row['Segmento'], NOMEPOSTO=row['NomePosto'], TIPOPOSTO=row['TipoPosto'], ENDERECO=row['Endereco'], NUMERO=row['Numero'], COMPLEMENTO=row['Complemento'], BAIRRO=row['Bairro'], CEP=row['Cep'], MUNICIPIOIBGE=row['MunicipioIbge'], MUNICIPIO=row['Municipio'], UF=row['UF'], DDD=row['DDD'], TELEFONE=row['Telefone'], CNPJASSIST=row['CnpjAssist'], NOMEASSIST=row['NomeAssist'], POSICAO=row['Posicao'])
                    print(posto_atendimento)
                    Criacao_Banco.session.add(posto_atendimento)

    #Confirmando as inserções no banco de dados
    Criacao_Banco.session.commit()

    # Ao final, abre o dashboard Streamlit no navegador
    os.system("start cmd /c streamlit run Dashborad.py")

except Exception as Ex:
    print(Ex)
finally:
    Criacao_Banco.session.close()
