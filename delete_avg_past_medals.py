import pandas as pd

# Load the dataset
medals_df = pd.read_csv('medals_by_country.csv')

# Drop the 'avg_past_medals' column if it exists
if 'avg_past_medals' in medals_df.columns:
    medals_df = medals_df.drop(columns=['avg_past_medals'])

# Save the updated dataset
medals_df.to_csv('medals_by_country.csv', index=False)
