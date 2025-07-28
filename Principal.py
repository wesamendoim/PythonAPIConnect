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

try:
    strRetorno = ConnAPIBancoCentral.retorno_Json()
    pprint.pprint(strRetorno)
    print(type(strRetorno))
    #strDataFrame = pd.read_excel("strDataFrame.xlsx")
    strRetorno_df = pd.DataFrame(strRetorno)
    pprint.pprint(strRetorno_df)
    linhasJson = strRetorno_df.to_dict(orient='records')


    for dados in linhasJson:
            #xiste = Criacao_Banco.session.query(Criacao_Banco.TBL_POSTO_ATENDIMENTO).filter_by(CNPJ=row['Cnpj']).first()
                    print(dados)
            #if not existe:
                #posto_atendimento = Criacao_Banco.TBL_POSTO_ATENDIMENTO(CNPJ=row['Cnpj'], NOMEIF=row['NomeIf'], SEGMENTO=row['Segmento'], NOMEPOSTO=row['NomePosto'], TIPOPOSTO=row['TipoPosto'], ENDERECO=row['Endereco'], NUMERO=row['Numero'], COMPLEMENTO=row['Complemento'], BAIRRO=row['Bairro'], CEP=row['Cep'], MUNICIPIOIBGE=row['MunicipioIbge'], MUNICIPIO=row['Municipio'], UF=row['UF'], DDD=row['DDD'], TELEFONE=row['Telefone'], CNPJASSIST=row['CnpjAssist'], NOMEASSIST=row['NomeAssist'], POSICAO=row['Posicao'])
                    posto_atendimento = Criacao_Banco.TBL_POSTO_ATENDIMENTO(
                        CNPJ=dados.get['Cnpj'],
                        NOMEIF=dados.get('NomeIf'),
                        SEGMENTO=dados.get('Segmento'),
                        NOMEPOSTO=dados.get('NomePosto'),
                        TIPOPOSTO=dados.get('TipoPosto'),
                        ENDERECO=dados.get('Endereco'),
                        NUMERO=dados.get('Numero'),
                        COMPLEMENTO=dados.get('Complemento'),
                        BAIRRO=dados.get('Bairro'),
                        CEP=dados.get('Cep'),
                        MUNICIPIOIBGE=dados.get('MunicipioIbge'),
                        MUNICIPIO=dados.get('Municipio'),
                        UF=dados.get('UF'),
                        DDD=dados.get('DDD'),
                        TELEFONE=dados.get('Telefone'),
                        CNPJASSIST=dados.get('CnpjAssist'),
                        NOMEASSIST=dados.get('NomeAssist'),
                        POSICAO=dados.get('Posicao')
                    )

                    print(posto_atendimento)
    Criacao_Banco.session.add(posto_atendimento)

          
    Criacao_Banco.session.commit()
    print("Dados inseridos com sucesso!")


except Exception as Ex:
    print(Ex)
finally:
    Criacao_Banco.session.close()
    #print(Ex.args.index())
