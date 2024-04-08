from base import *
import matplotlib.pyplot as plt
# Contagem de valores em falta para cada dataset

def missing_values(df, name):
    missing_values_count = df.isnull().sum()

    print(f"Valores em falta do dataset -> {name}:\n{missing_values_count}")
    return missing_values_count

missing_values(df1, 'Perth' )
missing_values(df2, 'Melbourne')
missing_values_df = missing_values(df,  'Dataset')



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

plot_missing_histogram(df1, 'Histograma de Valores Ausentes - Perth')
plot_missing_histogram(df2, 'Histograma de Valores Ausentes - Melbourne')
plot_missing_histogram(df, 'Histograma de Valores Ausentes - Dataset')


# Calcular a porcentagem de valores ausentes em relação aos valores presentes
total_values = len(df)
percentage_missing = (missing_values_df / total_values) * 100
percentage_present = 100 - percentage_missing

# Plotar gráfico circular
labels = ['Valores Presentes', 'Valores Ausentes']
sizes = [percentage_present.sum(), percentage_missing.sum()]
colors = ['lightgreen', 'coral']
explode = (0.1, 0)

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Porcentagem de Valores Presentes e Ausentes')
plt.axis('equal')
plt.show()

# Alterar valores ausentes numericos para a mediana, valores categóricos para a moda e remover linhas com mais de 3 características ausentes no dataset original
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        median = df[col].median()
        df[col] = df[col].fillna(median)
    else:
        mode = df[col].mode()[0]
        df.loc[:, col] = df[col].fillna(mode)

    # Remover linhas com mais de 3 craracterísticas ausentes
    df = df.dropna(thresh=len(df.columns) - 3)

# Plotar histograma de valores ausentes
plot_missing_histogram(df, 'Histograma de Valores Ausentes - Data sem Valores Ausentes')

# Salvar o dataset sem valores ausentes
df.to_csv('data/dataset_without_missing_values.csv', index=False)

missing_values_df = missing_values(df,  'Data sem Valores Ausentes')