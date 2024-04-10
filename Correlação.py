from base import *
import matplotlib.pyplot as plt
import seaborn as sns

# Função para plotar gráfico de correlação

numericas = df_final.select_dtypes(include=['int', 'float']).columns

correlacao = df_final[numericas].corr()

# Plotar o gráfico de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlação das Variáveis')
plt.show()
