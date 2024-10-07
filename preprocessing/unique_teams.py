# This script calculates the number of unique teams

import pandas as pd

df = pd.read_csv('medals_by_country.csv')
unique_teams = df['Team'].unique()
num_unique_teams = len(unique_teams)
print(f"Number of Unique Teams: {num_unique_teams}")