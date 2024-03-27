from base import *
import numpy as np


# calcular z-score para cada coluna com valores numéricos
threshold = 3
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    z = (df[col] - df[col].mean()) / np.std(df[col])
    outliers = df[z > threshold]

    # imprimir os outliers
    print(f"Outliers in column {col} with z-score > {threshold}:")
    print(outliers)
