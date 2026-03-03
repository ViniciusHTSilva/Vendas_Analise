# %%
import pandas as pd

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
# Proximo passo remover os dados NA.