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
cursor.execute(""" 
SELECT customer_state, SUM(receita) as total_receita FROM vendas GROUP BY customer_state ORDER BY total_receita DESC
""")

receitaestado = cursor.fetchall()

# Top 10 por receita
cursor.execute(""" 
SELECT product_category_name, SUM(receita) as receita_cat FROM vendas GROUP BY product_category_name ORDER BY receita_cat DESC
""")

top10 = cursor.fetchmany(10)

## Pedidos por mes/ano
cursor.execute(""" 
SELECT strftime('%Y-%m', order_purchase_timestamp) as mes_ano, COUNT(*) as qtd_pedidos FROM vendas GROUP BY mes_ano
""")

mesAno = cursor.fetchall()

#Receita Por Tipo
cursor.execute(""" 
SELECT payment_type, AVG(receita) as avg_receita FROM vendas GROUP BY payment_type
""")

ReceitaTipo = cursor.fetchall()


#Pedidos atrasados
cursor.execute("SELECT COUNT(*) *100.0 / (SELECT COUNT(*) FROM vendas) as pct_atrasados FROM vendas WHERE order_delivered_customer_date > order_estimated_delivery_date")

Atrasados = cursor.fetchall()


print(" -- RECEITA POR ESTADO --")
print(receitaestado)
print(" -- TOP 10 --")
print(top10)
print(" -- MES / ANO --")
print(mesAno)
print(" -- RECEITA TIPO --")
print(ReceitaTipo)
print(" -- ATRASADOS --")
print(Atrasados)

