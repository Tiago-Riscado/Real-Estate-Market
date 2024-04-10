from sklearn.preprocessing import MinMaxScaler
from base import *


# Função para normalizar os dados
def normaliza_dados(dados):

    colunas_numericas = dados.select_dtypes(include=['int', 'float']).columns

    escala = MinMaxScaler()

    normallizar = escala.fit_transform(dados[colunas_numericas])

    return normallizar


df_normalizado = normaliza_dados(df_final)

# print(df_normalizado)
