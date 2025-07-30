import pandas as pd

def test_db_connection():
    df = pd.read_sql('SELECT * FROM TBL_POSTO_ATENDIMENTO_V2', 'sqlite:///APIBancoCentral.db')
    assert not df.empty, "O DataFrame retornado do banco está vazio!"

def test_segmento_counts():
    df = pd.read_sql('SELECT * FROM TBL_POSTO_ATENDIMENTO_V2', 'sqlite:///APIBancoCentral.db')
    segmento_counts = df.groupby('SEGMENTO').size().reset_index(name='QtdPostos')
    assert 'SEGMENTO' in segmento_counts.columns
    assert 'QtdPostos' in segmento_counts.columns
    assert segmento_counts['QtdPostos'].sum() == len(df)
