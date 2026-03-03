# %%
import pandas as pd
import matplotlib as plt

df = pd.read_csv("./Dados/DadosLimpo.csv", sep=',')

df.head()

# %%
df.shape
# %%
df.describe
# %%
df.info()
# %%
## Tipos de Colunas
df.dtypes
# %%
#removendo os NA
df = df.dropna().drop_duplicates()
# %%

df.dtypes

# %%

#Convertendo para data 

colunas_data = [

    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
     
]

df[colunas_data] = df[colunas_data].apply(pd.to_datetime)
# %%

# Precisamos cirar uma coluna receita mas como nao temos a coluna de Quantity usaremos o payment

df["receita"] = df["payment_value"]

# %%
df

# %%
df.to_csv("dados_limpo2.csv", index=None)
# %%
