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

    # Clusterização por quantidade de postos por UF
    st.subheader("Clusterização dos Estados (UF) por Quantidade de Postos")
    uf_counts = df.groupby('UF').size().reset_index(name='QtdPostos')
    uf_counts = uf_counts[uf_counts['UF'].notnull() & (uf_counts['UF'] != '')]
    kmeans = KMeans(n_clusters=2, random_state=42)
    uf_counts['Cluster'] = kmeans.fit_predict(uf_counts[['QtdPostos']])

    # Mostra resultado em tabela
    st.dataframe(uf_counts)

    # Gráfico interativo
    fig = px.bar(uf_counts, x='UF', y='QtdPostos', color='Cluster', barmode='group',
                title='Quantidade de Postos por UF com Clusterização')
    st.plotly_chart(fig)

    # --- NOVO: Selecionar cluster e mostrar postos ---
    st.subheader("Visualizar Postos por Cluster")
    cluster_selected = st.selectbox("Selecione o Cluster:", sorted(uf_counts['Cluster'].unique()))

    # Descobre as UFs do cluster selecionado
    ufs_do_cluster = uf_counts[uf_counts['Cluster'] == cluster_selected]['UF'].tolist()
    # Filtra os postos dessas UFs
    postos_do_cluster = df[df['UF'].isin(ufs_do_cluster)]

    st.write(f"Postos pertencentes ao Cluster {cluster_selected}:")
    st.dataframe(postos_do_cluster)

    # Agrupa por Segmento e conta quantos postos tem em cada segmento
    segmento_counts = df.groupby('SEGMENTO').size().reset_index(name='QtdPostos')
    segmento_counts = segmento_counts[segmento_counts['SEGMENTO'].notnull() & (segmento_counts['SEGMENTO'] != '')]
    st.dataframe(segmento_counts)
    fig = px.bar(segmento_counts, x='SEGMENTO', y='QtdPostos', 
                title='Quantidade de Postos por Segmento')
    st.plotly_chart(fig)

    st.info("Você pode expandir este dashboard para usar outros algoritmos de IA, como previsão, classificação, análise de sentimentos, entre outros.")

    # --- NOVO: Selecionar UF e mostrar postos ---
    st.subheader("Visualizar Postos por UF")
    uf_selected = st.selectbox("Selecione a UF:", sorted(df['UF'].dropna().unique()))

    # Filtra os postos da UF selecionada
    postos_da_uf = df[df['UF'] == uf_selected]

    st.write(f"Postos pertencentes à UF {uf_selected}:")
    st.dataframe(postos_da_uf)

    st.subheader("Analise por CNPJ") 
    segmento_counts = df.groupby('CNPJ').size().reset_index(name='TipoPosto')
    segmento_counts = segmento_counts[segmento_counts['CNPJ'].notnull() & (segmento_counts['CNPJ'] != '')]
    st.dataframe(segmento_counts)
    fig = px.area(segmento_counts, x='CNPJ', y='TipoPosto', 
                title='Quantidade de Postos por CNPJ')
    st.plotly_chart(fig)

Dashboard()