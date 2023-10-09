#URL API Banco Central https://dadosabertos.bcb.gov.br/dataset?res_format=API
#Sintaxe da API https://olinda.bcb.gov.br/olinda/servico/mecir_moedas_comemorativas/versao/v1/odata/[codigo_recurso]?$format=json&[Outros Parâmetros]

# LINK IBGE https://servicodados.ibge.gov.br/api/docs

# https://servicodados.ibge.gov.br/api/v3/agregados/2259/periodos/201601/variaveis/1076?localidades=N7[3501]

import ssl
import requests

link = "https://servicodados.ibge.gov.br/api/v3/agregados/2259/periodos/201601/variaveis/1076?localidades=N7[3501]"

requisicao = requests.get(link)

print(requisicao.json)()
