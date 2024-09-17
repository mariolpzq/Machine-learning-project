import pandas as pd

# Load the datasets
medals_df = pd.read_csv('medals_by_country.csv')
olympics_df = pd.read_csv('olympics_dataset.csv')

# Create a mapping for NOC codes from the olympics dataset
noc_mapping = olympics_df[['Team', 'NOC']].drop_duplicates()
noc_mapping = noc_mapping.set_index('Team')['NOC'].to_dict()

# Create a mapping for Host countries based on the year
host_mapping = olympics_df[['Year', 'Host country']].drop_duplicates()
host_mapping = host_mapping.set_index('Year')['Host country'].to_dict()

# Map NOC codes to medals_df
medals_df['NOC'] = medals_df['Team'].map(noc_mapping)

# Map Host countries to medals_df
medals_df['Host country'] = medals_df['Year'].map(host_mapping)

# Save the updated dataframe to a new CSV
medals_df.to_csv('updated_medals_my_country.csv', index=False)
