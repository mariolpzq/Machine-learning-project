import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'olympics_dataset.csv'
df = pd.read_csv(file_path, encoding='utf-8', delimiter=';')

# Define the mapping of cities to ISO 3166-1 alpha-3 codes
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

print("ISO codes have been assigned and the CSV file has been updated.")
