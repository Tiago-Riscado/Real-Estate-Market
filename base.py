import pandas as pd
import numpy as np


# Criação das dataframes
path1 = r"data\all_perth_310121.csv"
path2 = r"data\Melbourne_housing_FULL.csv"
#path3 = r"data\NY-House-Dataset.csv"

df1 = pd.read_csv(path1)
df2 = pd.read_csv(path2)
#df3 = pd.read_csv(path3)

# Renomeação das colunas
df1 = df1.rename(columns={'LAND_AREA': 'Landsize'})
df2 = df2.rename(columns={'Bedroom2': 'BEDROOMS', 'Bathroom': 'BATHROOMS', 'Car': 'GARAGE', 'YearBuilt': 'BUILD_YEAR', 'Address': 'ADDRESS', 'Price': 'PRICE', 'Suburb': 'SUBURB', 'Postcode': 'POSTCODE', 'Lattitude': 'LATITUDE', 'Longtitude': 'LONGITUDE', 'Date': 'DATE_SOLD'})
#df3 = df3.rename(columns={'BEDS': 'BEDROOMS', 'BATH': 'BATHROOMS', 'PROPERTYSQFT': 'Landsize', })

# Remoção de colunas
df1 = df1.drop(columns={'FLOOR_AREA', 'CBD_DIST', 'NEAREST_STN', 'NEAREST_STN_DIST', 'NEAREST_SCH', 'NEAREST_SCH_DIST', 'NEAREST_SCH_RANK'})
df2 = df2.drop(columns={'Rooms', 'Type', 'Method', 'SellerG', 'BuildingArea', 'CouncilArea', 'Regionname', 'Propertycount', 'Distance'})
#df3 = df3.drop(columns={'BROKERTITLE', 'TYPE', 'STATE', 'MAIN_ADDRESS', 'ADMINISTRATIVE_AREA_LEVEL_2', 'LOCALITY', 'SUBLOCALITY', 'STREET_NAME', 'LONG_NAME', 'FORMATTED_ADDRESS' } )

# Concatenação das dataframes
df = pd.concat([df1, df2], ignore_index=True)

# Conversão de float para inteiro

numeric_columns = ['PRICE', 'POSTCODE', 'BEDROOMS', 'BATHROOMS', 'GARAGE', 'BUILD_YEAR']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce').round(decimals=0).astype('Int64')

df['DATE_SOLD'] = pd.to_datetime(df['DATE_SOLD'], errors='coerce')

# Formatar a coluna de data como "dia/mês/ano"
df['DATE_SOLD'] = df['DATE_SOLD'].dt.strftime('%d/%m/%Y')
# Remover colunas vazias

# Criação do dataset file
df.to_csv('data/dataset.csv', index=False)

# Carregar o dataset
df = pd.read_csv('data/dataset.csv', low_memory=False)

