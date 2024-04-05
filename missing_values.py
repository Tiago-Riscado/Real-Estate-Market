from base import *
import matplotlib.pyplot as plt
# Contagem de valores em falta

missing_values = df.isnull().sum()
#print(missing_values)

missing_values1 = df1.isnull().sum()
missing_values2 = df2.isnull().sum()
missing_values3 = df3.isnull().sum()
# print(missing_values1)
# print(missing_values2)
# print(missing_values3)


