import pandas as pd

# Load the dataset
medals_df = pd.read_csv('medals_by_country.csv')

# Create the "isHost" column
medals_df['isHost'] = (medals_df['NOC'] == medals_df['Host country']).astype(int)

# Save the updated dataframe to a new CSV
medals_df.to_csv('medals_by_country.csv', index=False)
