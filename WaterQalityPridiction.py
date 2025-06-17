import pandas as pd #dataframe manipulation
import numpy as np #numerical operations
from sklearn.multioutput import MultiOutputRegressor #multi-output regression,implementing multiple models 
from sklearn.ensemble import RandomForestRegressor #random forest regressor
from sklearn.model_selection import train_test_split #train-test split
from sklearn.metrics import mean_squared_error, r2_score #evaluation metrics 

df =pd.read_csv('PB_ALL_2000_2021.csv',sep=';') #load dataset
print(df)

df.info()# print dataset info
print(df.shape)
print(df.describe().T)# print dataset description and convert rows to columns

# mising values
print(df.isnull().sum()) # print missing values in each column

 #convert date column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
df.info() # print dataset info after conversion

df=df.sort_values(by=['id','date'])# sort values by id and date
print(df.head())

df['year'] = df['date'].dt.year # extract year from date
df['month'] = df['date'].dt.month # extract month from date
print(df.head())

print(df.columns)
pollutants = ['NH4', 'BSK5', 'Suspended', 'O2', 'NO3', 'NO2', 'SO4', 
'PO4', 'CL', 'year']
print(pollutants)