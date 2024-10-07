# This script assigns ISO codes to the host countries' cities in the dataset

import pandas as pd

file_path = 'olympics_dataset.csv'
df = pd.read_csv(file_path, encoding='utf-8', delimiter=';')

city_to_iso = {
    'Barcelona': 'ESP',
    'London': 'GBR',
    'Sydney': 'AUS',
    'Atlanta': 'USA',
    'Beijing': 'CHN',
    'Rio de Janeiro': 'BRA',
    'Athina': 'GRC',
    'Los Angeles': 'USA',
    'Seoul': 'KOR',
    'Tokyo': 'JPN',
    'Paris': 'FRA'
}

df['Host country'] = df['City'].map(city_to_iso)
df.to_csv(file_path, index=False)
