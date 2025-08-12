import unittest
import Criacao_Banco
import pandas as pd

class TestPrincipal(unittest.TestCase):
    def setUp(self):
        # Cria um DataFrame de teste
        self.df = pd.DataFrame([{
            'Cnpj': '12345678',
            'NomeIf': 'Teste',
            'Segmento': 'Teste',
            'NomePosto': 'Posto Teste',
            'TipoPosto': 'Tipo',
            'Endereco': 'Rua Teste',
            'Numero': '1',
            'Complemento': '',
            'Bairro': 'Centro',
            'Cep': '00000-000',
            'MunicipioIbge': '1234567',
            'Municipio': 'Cidade',
            'UF': 'SP',
            'DDD': '11',
            'Telefone': '999999999',
            'CnpjAssist': '87654321',
            'NomeAssist': 'Assistente',
            'Posicao': '01/01/2025'
        }])

    def test_insercao(self):
        # Tenta inserir no banco
        for _, row in self.df.iterrows():
            existe = Criacao_Banco.session.query(Criacao_Banco.TBL_POSTO_ATENDIMENTO).filter_by(CNPJ=row['Cnpj']).first()
            if not existe:
                posto = Criacao_Banco.TBL_POSTO_ATENDIMENTO(
                    CNPJ=row['Cnpj'],
                    NOMEIF=row['NomeIf'],
                    SEGMENTO=row['Segmento'],
                    NOMEPOSTO=row['NomePosto'],
                    TIPOPOSTO=row['TipoPosto'],
                    ENDERECO=row['Endereco'],
                    NUMERO=row['Numero'],
                    COMPLEMENTO=row['Complemento'],
                    BAIRRO=row['Bairro'],
                    CEP=row['Cep'],
                    MUNICIPIOIBGE=row['MunicipioIbge'],
                    MUNICIPIO=row['Municipio'],
                    UF=row['UF'],
                    DDD=row['DDD'],
                    TELEFONE=row['Telefone'],
                    CNPJASSIST=row['CnpjAssist'],
                    NOMEASSIST=row['NomeAssist'],
                    POSICAO=row['Posicao']
                )
                Criacao_Banco.session.add(posto)
        Criacao_Banco.session.commit()

        # Verifica se foi inserido
        result = Criacao_Banco.session.query(Criacao_Banco.TBL_POSTO_ATENDIMENTO).filter_by(CNPJ='12345678').first()
        self.assertIsNotNone(result)

    def tearDown(self):
        # Remove o registro de teste
        Criacao_Banco.session.query(Criacao_Banco.TBL_POSTO_ATENDIMENTO).filter_by(CNPJ='12345678').delete()
        Criacao_Banco.session.commit()

if __name__ == '__main__':
    unittest.main()