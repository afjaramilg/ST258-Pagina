import pandas as pd
import numpy as np

data_energy= pd.read_csv("energy_dataset.csv")
data_weather=pd.read_csv("weather_features.csv")

#data energy
print(data_energy.isnull().sum())
#data weather
print(data_weather.isnull().sum())

#tumbar las columnas nulas
data_energy = data_energy.drop(['generation hydro pumped storage aggregated','forecast wind offshore eday ahead'],1)
data_energy=data_energy.dropna()

print(data_energy.isnull().sum())
print(data_weather.describe())
print(data_energy.describe())

data_energy = data_energy.drop(['generation fossil coal-derived gas','generation fossil oil shale','generation fossil peat','generation geothermal','generation marine','generation wind offshore'],1)
print(data_energy.head())
print(data_energy.describe())


data_energy.to_csv('clean_energy.csv')
data_weather.to_csv('clean_weather.csv')


