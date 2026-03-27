
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



st.set_page_config(layout="wide")
import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.stApp {
    background: #0f172a;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""

            
<h1 style='text-align: center;
            color:White'>
            Analise de Vendas
            </h1>

""",unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3, gap='large')





with col1:
##  Receita
    st.markdown("""
        <div style="
            background-color: red;
            border-radius: 10px;
            border: 1px solid white;
            width: 110%;
        ">
    """, unsafe_allow_html=True)

    st.bar_chart(df_Receita.set_index("Estado"))

    st.markdown("</div>", unsafe_allow_html=True)
with col2:
##  Top10
    st.dataframe(df_Top10, hide_index=True)
with col3:
##  Mes/Ano
    st.bar_chart(df_Mes_Ano.set_index("Mes / Ano"))


col4, col5 = st.columns(2, gap='large')

with col4:
##  Tipo Receita 
    fig = px.pie(
    df_ReceitaTipo,
    names="payment_type",
    values="avg_receita",
    title="Modelo Receita"
    )
    st.plotly_chart(fig)
with col5:
    st.dataframe(df_Atrasados, hide_index=True)