
import streamlit as st
import pandas as pd
import plotly.express as px


df_Receita = pd.read_excel("../Dados/AnaliseFilnal.xlsx", sheet_name="Receita")
df_Top10 = pd.read_excel("../Dados/AnaliseFilnal.xlsx", sheet_name="Top10")
df_Mes_Ano = pd.read_excel("../Dados/AnaliseFilnal.xlsx", sheet_name="Mes_Ano")
df_ReceitaTipo = pd.read_excel("../Dados/AnaliseFilnal.xlsx", sheet_name="ReceitaTipo")
df_Atrasados = pd.read_excel("../Dados/AnaliseFilnal.xlsx", sheet_name="Atrasados")

#Renomeando as Colunas
df_Receita = df_Receita.rename(columns={
    "customer_state":"Estado",
    "total_receita":"Receita",
})

df_Top10 = df_Top10.rename(columns={
    "product_category_name":"Produto",
    "receita_cat":"Receita Categoria",
})

df_Mes_Ano = df_Mes_Ano.rename(columns={
    "mes_ano": "Mes / Ano",
    "qtd_pedidos": "Quantidade de Pedidos",
})
df_Atrasados = df_Atrasados.rename(columns={
    "pct_atrasados": "Pagamento Atrasado",

})






st.markdown('''
Analise de :green[Vendas]
''')


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Receita","Top10","Mes/Ano","Tipo Receita","Atrasados"])


with tab1:
##  Receita
    st.bar_chart(df_Receita.set_index("Estado"))
with tab2:
##  Top10
    st.dataframe(df_Top10, hide_index=True)
with tab3:
##  Mes/Ano
    st.bar_chart(df_Mes_Ano.set_index("Mes / Ano"))
with tab4:
##  Tipo Receita 
    fig = px.pie(
    df_ReceitaTipo,
    names="payment_type",
    values="avg_receita",
    title="Modelo Receita"
    )
    st.plotly_chart(fig)
with tab5:
    st.dataframe(df_Atrasados, hide_index=True)
