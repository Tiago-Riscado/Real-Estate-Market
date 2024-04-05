import matplotlib.pyplot as plt
import seaborn as sns
from base import *

columns = df.select_dtypes(include=['int', 'float']).columns

for i, col1 in enumerate(columns):
    for j, col2 in enumerate(columns):
        if i != j:
            plt.figure(figsize=(8, 6))
            sns.scatterplot(x=col1, y=col2, data=df)
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title(f'Scatter plot: {col1} vs {col2}')
            plt.show()

