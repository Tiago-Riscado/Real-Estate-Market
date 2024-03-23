import pandas as pd
import numpy as np

#Criação das dataframes

path1 = r"data\all_perth_310121.csv"
path2 = r"data\Melbourne_housing_FULL.csv"
path3 = r"data\melbourne_housing.csv"

df1 = pd.read_csv(path1)
df2 = pd.read_csv(path2)
df3 = pd.read_csv(path3)

# Renomeação das colunas
df1 = df1.rename(columns={'LAND_AREA': 'Landsize'})
df2 = df2.rename(columns={'Bedroom2': 'BEDROOMS', 'Bathrooms': 'BATHROOMS', 'Car': 'GARAGE', 'YearBuilt': 'BUILD_YEAR', 'Address': 'ADDRESS', 'Price': 'PRICE', 'Suburb': 'SUBURB', 'Postcode': 'POSTCODE', 'Lattitude': 'LATITUDE', 'Longtitude': 'LONGITUDE'})
df3 = df2.rename(columns={'Bedroom2': 'BEDROOMS', 'Bathrooms': 'BATHROOMS', 'Car': 'GARAGE', 'YearBuilt': 'BUILD_YEAR', 'Address': 'ADDRESS', 'Price': 'PRICE', 'Suburb': 'SUBURB', 'Postcode': 'POSTCODE', 'Lattitude': 'LATITUDE', 'Longtitude': 'LONGITUDE'})

# Remoção de colunas
df1 = df1.drop(columns={'FLOOR_AREA', 'CBD_DIST', 'NEAREST_STN', 'NEAREST_STN_DIST', 'NEAREST_SCH', 'NEAREST_SCH_DIST', 'NEAREST_SCH_RANK'})
df2 = df2.drop(columns={'Rooms', 'Type', 'Method', 'SellerG', 'BuildingArea', 'CouncilArea', 'Regionname', 'Propertycount', 'Distance'})
df3 = df3.drop(columns= {'Rooms', 'Type', 'Method', 'SellerG', 'BuildingArea', 'CouncilArea', 'Regionname', 'Propertycount', 'Distance'})

# Concatenação das dataframes
df = pd.concat([df1, df2, df3], ignore_index=True)

# Substituir valores não finitos (NaN, infinito) por NaN
df['PRICE'] = df['PRICE'].replace([np.inf, -np.inf], np.nan)
df['POSTCODE'] = df['POSTCODE'].replace([np.inf, -np.inf], np.nan)
df['BEDROOMS'] = df['BEDROOMS'].replace([np.inf, -np.inf], np.nan)
df['BATHROOMS'] = df['BATHROOMS'].replace([np.inf, -np.inf], np.nan)
df['GARAGE'] = df['GARAGE'].replace([np.inf, -np.inf], np.nan)
df['BUILD_YEAR'] = df['BUILD_YEAR'].replace([np.inf, -np.inf], np.nan)

# Conversão de floar para inteiro

df['PRICE'] = pd.to_numeric(df['PRICE'], errors='coerce').astype(pd.Int64Dtype())
df['POSTCODE'] = pd.to_numeric(df['POSTCODE'], errors='coerce').astype(pd.Int64Dtype())
df['BEDROOMS'] = pd.to_numeric(df['BEDROOMS'], errors='coerce').astype(pd.Int64Dtype())
df['BATHROOMS'] = pd.to_numeric(df['BATHROOMS'], errors='coerce').astype(pd.Int64Dtype())
df['GARAGE'] = pd.to_numeric(df['GARAGE'], errors='coerce').astype(pd.Int64Dtype())
df['BUILD_YEAR'] = pd.to_numeric(df['BUILD_YEAR'], errors='coerce').astype(pd.Int64Dtype())

# Remoção de linhas com valores nulos
df = df.drop(columns={'Date', 'Bathroom'})

#Criação do dataset file

df.to_csv('data/dataset.csv', index=False)

# Carregar o dataset
df = pd.read_csv('data/dataset.csv', low_memory=False)