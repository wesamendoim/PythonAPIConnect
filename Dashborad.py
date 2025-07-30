import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px

def Dashboard():
    # Leitura dos dados
    df = pd.read_sql('SELECT * FROM TBL_POSTO_ATENDIMENTO_V2', 'sqlite:///APIBancoCentral.db')

    st.title("Dashboard Postos de Atendimento com IA")

    st.subheader("Tabela de Dados")
    st.dataframe(df)

    # Exemplo de clusterização por quantidade de postos por UF
    st.subheader("Clusterização dos Estados (UF) por Quantidade de Postos")

    # Agrupa por UF e conta quantos postos tem em cada estado
    uf_counts = df.groupby('UF').size().reset_index(name='QtdPostos')

    # Remove UFs nulas ou vazias
    uf_counts = uf_counts[uf_counts['UF'].notnull() & (uf_counts['UF'] != '')]

    # Clusterização (2 clusters como exemplo)
    kmeans = KMeans(n_clusters=2, random_state=42)
    uf_counts['Cluster'] = kmeans.fit_predict(uf_counts[['QtdPostos']])

    # Mostra resultado em tabela
    st.dataframe(uf_counts)

    # Gráfico interativo
    fig = px.bar(uf_counts, x='UF', y='QtdPostos', color='Cluster', barmode='group',
                title='Quantidade de Postos por UF com Clusterização')
    st.plotly_chart(fig)

    # Agrupa por Segmento e conta quantos postos tem em cada segmento
    segmento_counts = df.groupby('SEGMENTO').size().reset_index(name='QtdPostos')

    # Remove segmentos nulos ou vazios
    segmento_counts = segmento_counts[segmento_counts['SEGMENTO'].notnull() & (segmento_counts['SEGMENTO'] != '')]

    # Mostra resultado em tabela
    st.dataframe(segmento_counts)

    # Gráfico interativo por segmento
    fig = px.bar(segmento_counts, x='SEGMENTO', y='QtdPostos', 
                title='Quantidade de Postos por Segmento')
    st.plotly_chart(fig)

    st.info("Você pode expandir este dashboard para usar outros algoritmos de IA, como previsão, classificação, análise de sentimentos, entre outros.")


Dashboard()