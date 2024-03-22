from base import *

# Contagem de valores em falta

missing_values = df.isnull().sum()
print(missing_values)

