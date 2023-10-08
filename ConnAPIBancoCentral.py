#URL API Banco Central https://dadosabertos.bcb.gov.br/dataset?res_format=API

#Sintaxe da API https://olinda.bcb.gov.br/olinda/servico/mecir_moedas_comemorativas/versao/v1/odata/[codigo_recurso]?$format=json&[Outros Parâmetros]

import requests

link = 'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$orderby=Data%20desc&$format=json'

requisicao = requests.get(link)

print(requisicao)