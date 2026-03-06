import sqlite3
import pandas as pd


# Conectando ao banco / Criando
conn = sqlite3.connect("./Banco/AnaliseVendas.db")

# Criar cursor
cursor = conn.cursor()
# lendo planilha com pandas

df = pd.read_csv("./Dados/dados_limpo2.csv", sep=",")

print(df.head())

# Colocando os dados do csv em um db 

df.to_sql("Vendas", conn, if_exists="replace", index=False)


## fazendo pesquisa no Banco de dados

#fetchall()  Retorna todos os dados
#fetchone() Retorna apenas uma linha
#fetchmany(n) Retorna o Valor que voce escolhe como o LIMIT

# Receita total por Estado
receitaestado = """ 
SELECT customer_state, SUM(receita) as total_receita FROM vendas GROUP BY customer_state ORDER BY total_receita DESC
"""


# Top 10 por receita
top10 = """ 
SELECT product_category_name, SUM(receita) as receita_cat FROM vendas GROUP BY product_category_name ORDER BY receita_cat DESC
"""


## Pedidos por mes/ano
mesAno = """ 
SELECT strftime('%Y-%m', order_purchase_timestamp) as mes_ano, COUNT(*) as qtd_pedidos FROM vendas GROUP BY mes_ano
"""

#Receita Por Tipo
ReceitaTipo = """ 
SELECT payment_type, AVG(receita) as avg_receita FROM vendas GROUP BY payment_type
"""

#Pedidos atrasados
Atrasados ="SELECT COUNT(*) *100.0 / (SELECT COUNT(*) FROM vendas) as pct_atrasados FROM vendas WHERE order_delivered_customer_date > order_estimated_delivery_date"






df_receita = pd.read_sql_query(receitaestado, conn)
df_top10 = pd.read_sql_query(top10, conn)
df_mesAno= pd.read_sql_query(mesAno, conn)
df_RecitaTipo = pd.read_sql_query(ReceitaTipo, conn)
df_Atrasados = pd.read_sql_query(Atrasados, conn)

print("RECEITA POR QUERY NO PANDAS" )
print(df_receita.head())
print(" -- TOP 10 --")
print(df_top10)
print(" -- MES / ANO --")
print(df_mesAno)
print(" -- RECEITA TIPO --")
print(df_RecitaTipo)
print(" -- ATRASADOS --")
print(df_Atrasados)


# Salvano as pesquisa por Query em um csv ou xlsx

with pd.ExcelWriter("./Dados/AnaliseFilnal.xlsx") as writer:
    df_receita.to_excel(writer, sheet_name="Receita", index=False)
    df_top10.to_excel(writer, sheet_name="Top10", index=False)
    df_mesAno.to_excel(writer, sheet_name="Mes_Ano", index=False)
    df_RecitaTipo.to_excel(writer, sheet_name="ReceitaTipo", index=False)
    df_Atrasados.to_excel(writer, sheet_name="Atrasados", index=False)