import pandas as pd

# Load the datasets
medals_df = pd.read_csv('medals_by_athlete.csv')
olympics_df = pd.read_csv('olympics_dataset.csv')

# Step 1: Create a mapping for NOC codes from the olympics dataset
noc_mapping = olympics_df[['Team', 'NOC']].drop_duplicates()
noc_mapping = noc_mapping.set_index('Team')['NOC'].to_dict()

# Add NOC column to medals_df
medals_df['NOC'] = medals_df['Team'].map(noc_mapping)

# Step 2: Create a mapping for Host country based on Year from olympics_df
host_mapping = olympics_df[['Year', 'Host country']].drop_duplicates()
host_mapping = host_mapping.set_index('Year')['Host country'].to_dict()

# Create the "isHost" column
medals_df['isHost'] = (medals_df['NOC'] == medals_df['Year'].map(host_mapping)).astype(int)

# Save the updated dataframe
medals_df.to_csv('medals_by_athlete.csv', index=False)
