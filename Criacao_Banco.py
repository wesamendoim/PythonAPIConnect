from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine('sqlite:///APIBancoCentral.db')

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class TBL_POSTO_ATENDIMENTO(Base):
    __tablename__ = 'TBL_POSTO_ATENDIMENTO'
    CNPJ = Column("CNPJ", primary_key=True)
    NOMEIF = Column("NOMEIF", String)
    SEGMENTO = Column("SEGMENTO", String(100))
    NOMEPOSTO = Column("NOMEPOSTO", String(100))
    TIPOPOSTO = Column("TIPOPOSTO", String(100))
    ENDERECO = Column("ENDERECO", String(100))
    NUMERO = Column("NUMERO", String(10))
    COMPLEMENTO = Column("COMPLEMENTO", String(100))
    BAIRRO = Column("BAIRRO", String(100))
    CEP = Column("CEP", String(10))
    MUNICIPIOIBGE = Column("MUNICIPIOIBGE", String(10))
    MUNICIPIO = Column("MUNICIPIO", String(100))
    UF = Column("UF", String(2))
    DDD = Column("DDD",String(2))
    TELEFONE = Column("TELEFONE", String(9))
    CNPJASSIST = Column("CNPJASSIST", String(14))
    NOMEASSIST = Column("NOMEASSIST", String(100))
    POSICAO = Column("POSICAO", String(100))

    def __init__(self, CNPJ,NOMEIF):

Base.metadata.create_all(bind=db)
