#importação
from base import *
import matplotlib.pyplot as plt
import seaborn as sns
import time
#selecionar colunas do dataset que contêm dados numéricos (inteiros ou float)
columns = df_fix.select_dtypes(include=['int', 'float']).columns

#método IQR
#calcular quartis
Q1 = df_fix[columns].quantile(0.25)
Q3 = df_fix[columns].quantile(0.75)

#calcular amplitude interquartil
IQR = Q3 -Q1

#calcular os limites inferior e superior
lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR

#determinação dos outliers (se o valor for inferior ao limite inferior ou superior ao limite superior)
outliers = (df_fix[columns] < lim_inf) | (df_fix[columns] > lim_sup)

#número de outliers por coluna
num_outliers_col = outliers.sum()

print("Quantidade de Outliers:")
print(num_outliers_col)

#Gráficos de dispersão
for i, col1 in enumerate(columns):
    for j, col2 in enumerate(columns):
        if i != j:
            plt.figure(figsize=(9,9))
            sns.scatterplot(x=col1, y=col2, data=df_fix)
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title(f'Scatter plot: {col1} vs {col2}')
            plt.show()

