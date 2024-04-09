# Importação
from base import *
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Selecionar colunas do dataset que contêm dados numéricos (inteiros ou float)
columns = df_fix.select_dtypes(include=['int', 'float']).columns

# Método IQR
# Calcular quartis
Q1 = df_fix[columns].quantile(0.25)
Q3 = df_fix[columns].quantile(0.75)

# Calcular amplitude interquartil
IQR = Q3 - Q1

# Calcular os limites inferior e superior
lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR


def contar_outliers(df):
    for col in columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lim_inf = Q1 - 1.5 * IQR
            lim_sup = Q3 + 1.5 * IQR
            outliers = (df[col] < lim_inf) | (df[col] > lim_sup)
            print(f'{col}: {outliers.sum()}')

    return


print('Contagem de outliers antes da remoção:')
contar_outliers(df_fix)

outliers = (df_fix[columns] < lim_inf) | (df_fix[columns] > lim_sup)

# Gráficos de dispersão
for i, col1 in enumerate(columns):
    for j, col2 in enumerate(columns):
        if i < j:
             plt.figure(figsize=(9, 9))
             sns.scatterplot(x=col1, y=col2, data=df_fix)
             plt.xlabel(col1)
             plt.ylabel(col2)
             plt.title(f'Scatter plot: {col1} vs {col2}')
             plt.show()


# Remoção dos outliers com o método IQR
# Substituição dos outliers pela mediana
for col in columns:
    df_fix[col] = np.where(outliers[col], df_fix[col].median(), df_fix[col])

# Contagem de outliers após a remoção
outliers_apos = (df_fix[columns] < lim_inf) | (df_fix[columns] > lim_sup)
num_outliers_col_apos = outliers_apos.sum()

print("Quantidade de Outliers após remoção:")
print(num_outliers_col_apos)


# Transformar valores numéricos para inteiros
numeric_columns = ['PRICE', 'POSTCODE', 'BEDROOMS', 'BATHROOMS', 'GARAGE', 'BUILD_YEAR']
for col in numeric_columns:
    df_fix[col] = pd.to_numeric(df_fix[col], errors='coerce').round(decimals=0).astype('Int64')

# Salvar o dataset sem outliers em um arquivo CSV
df_fix.to_csv('data/dataset_final.csv', index=False)
