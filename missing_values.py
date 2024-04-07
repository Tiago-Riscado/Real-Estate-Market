from base import *
import matplotlib.pyplot as plt
# Contagem de valores em falta

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


def plot_frequency_table_with_intervals(column):
    # Definir os intervalos de anos
    intervals = [0, 1970, 1980, 1990, 2000, 2010, df[column].max() + 1]
    interval_labels = ['<1970', '1970-1980', '1980-1990', '1990-2000', '2000-2010', '2010+']

    # Categorizar os anos de construção em intervalos
    df['Year Interval'] = pd.cut(df[column], bins=intervals, labels=interval_labels)

    # Calcular a tabela de frequência com base nos intervalos
    frequency_table = df['Year Interval'].value_counts().reset_index()
    frequency_table.columns = ['Year Interval', 'Frequência']

    # Exibir a tabela de frequência em uma janela separada
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')  # Desativar os eixos
    ax.table(cellText=frequency_table.values, colLabels=frequency_table.columns, loc='center')
    plt.title(f"Tabela de Frequência para o ano de construção")
    plt.show()


# Exibir a tabela de frequência com intervalos para o ano de construção
plot_frequency_table_with_intervals("BUILD_YEAR")
# Alterar valores ausentes para a moda da coluna e salvar o dataset em ficheriro CSV

for col in df.columns:
    mode = df[col].mode()[0]
    df[col].fillna(mode, inplace=True)





plot_missing_histogram(df, 'Histograma de Valores Ausentes - Data sem Valores Ausentes')

df.to_csv('data/dataset_without_missing_values.csv', index=False)
missing_values_df = missing_values(df,  'Data sem Valores Ausentes')