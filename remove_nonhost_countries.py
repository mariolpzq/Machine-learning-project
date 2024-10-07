import pandas as pd

# Load your dataset
df = pd.read_csv('medals_by_country.csv')

# Filter rows where NOC is 'USA'
df_filtered = df[df['NOC'].isin(['USA', 'ESP', 'KOR', 'JPN', 'GBR', 'FRA', 'CHN', 'BRA', 'AUS'])]

# Save the filtered dataset to a new CSV file
df_filtered.to_csv('filtered_medals_by_country.csv', index=False)