from base import *
import matplotlib.pyplot as plt
import seaborn as sns

columns = df.select_dtypes(include=['int', 'float']).columns

Q1 = df[columns].quantile(0.25)
Q3 = df[columns].quantile(0.75)

IQR = Q3 -Q1

limite_inf = Q1 - 1.5 * IQR
limite_sup = Q3 + 1.5 * IQR

outliers = (df[columns] < limite_inf) | (df[columns] > limite_sup)

num_outliers_col = outliers.sum()

print("Quantidade de Outliers:")
print(num_outliers_col)

# Plotar gráficos de dispersão para cada coluna
for col in columns:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df.index, y=df[col], hue=outliers[col], palette='Set2')
    plt.title(f'Dispersão de {col}')
    plt.xlabel('Índice')
    plt.ylabel(col)
    plt.legend(title='Outlier', loc='upper right')
    plt.show()

