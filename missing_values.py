from base import *
import matplotlib.pyplot as plt
# Contagem de valores em falta

missing_values = df.isnull().sum()
print(missing_values)

missing_values1 = df1.isnull().sum()
missing_values2 = df2.isnull().sum()
#missing_values3 = df3.isnull().sum()
print(missing_values1)
print(missing_values2)
#print(missing_values3)

# Função para plotar histograma de valores ausentes
def plot_missing_histogram(dataframe, title):
    missing_values_count = dataframe.isnull().sum()
    plt.figure(figsize=(10, 6))
    plt.bar(missing_values_count.index, missing_values_count.values, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel('Colunas')
    plt.ylabel('Contagem de Valores Ausentes')
    plt.xticks(rotation=45)
    plt.show()

# Plotar histograma de valores ausentes para o primeiro conjunto de dados (Perth)
plot_missing_histogram(df1, 'Histograma de Valores Ausentes - Perth')

# Plotar histograma de valores ausentes para o segundo conjunto de dados (Melbourne)
plot_missing_histogram(df2, 'Histograma de Valores Ausentes - Melbourne')

# Plotar histograma de valores ausentes para o dataset final
plot_missing_histogram(df, 'Histograma de Valores Ausentes - Dataset')



