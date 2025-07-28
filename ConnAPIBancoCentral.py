#URL API Banco Central https://dadosabertos.bcb.gov.br/dataset?res_format=API
#Sintaxe da API https://olinda.bcb.gov.br/olinda/servico/mecir_moedas_comemorativas/versao/v1/odata/[codigo_recurso]?$format=json&[Outros Parâmetros]
# LINK IBGE https://servicodados.ibge.gov.br/api/docs

# https://servicodados.ibge.gov.br/api/v3/agregados/2259/periodos/201601/variaveis/1076?localidades=N7[3501]

import requests
import pandas as pd

#link = "https://olinda.bcb.gov.br/olinda/servico/Informes_PostosDeAtendimento/versao/v1/odata/PostosAtendimento?$top=100&$format=json&$select=Cnpj,NomeIf,Segmento,NomePosto,TipoPosto,Endereco,Numero,Complemento,Bairro,Cep,MunicipioIbge,Municipio,UF,DDD,Telefone,CnpjAssist,NomeAssist,Posicao"

import requests
import pandas as pd

def retorno_Json(*args):
    link = "https://olinda.bcb.gov.br/olinda/servico/Informes_PostosDeAtendimento/versao/v1/odata/PostosAtendimento?$top=100&$format=json&$select=Cnpj,NomeIf,Segmento,NomePosto,TipoPosto,Endereco,Numero,Complemento,Bairro,Cep,MunicipioIbge,Municipio,UF,DDD,Telefone,CnpjAssist,NomeAssist,Posicao"
    requisicao = requests.get(link, verify=False)

    if requisicao.status_code == 200:
        return requisicao.json()
    else:
        raise ValueError('Conexão falhou')

# Exemplo de como chamar a função
# resultado = retorno_Json()
# print(resultado)
