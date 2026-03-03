# %% 
import pandas as pd
import matplotlib as plt


df = pd.read_csv("./Dados/dados_limpo2.csv", sep=',')

# %%

## Fazendo um Histograma Simples

df["receita"].hist(bins=50)

plt.show()
# %%


## Top 10 
## Usando o Value conts para fazer a contagem
top = df['product_category_name'].value_counts().head(10); top.plot(kind='bar')


# %%

# Scatter
df.plot.scatter(x='price', y='freight_value')
# %%

