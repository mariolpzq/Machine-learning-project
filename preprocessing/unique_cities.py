# This script calculates the number of unique cities

import pandas as pd

file_path = 'olympics_dataset.csv'
df = pd.read_csv(file_path)
unique_cities = df['City'].unique()

print("Unique Cities:")
for city in unique_cities:
    print(city)