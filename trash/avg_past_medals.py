import pandas as pd

# Load the dataset
medals_df = pd.read_csv('medals_by_country.csv')

# Step 1: Calculate total medals for each year
medals_df['Total_medals'] = medals_df['Gold'] + medals_df['Silver'] + medals_df['Bronze']

# Step 2: Filter non-host years (isHost == 0)
non_host_years = medals_df[medals_df['isHost'] == 0]

# Step 3: Calculate avg_past_medals for each country (NOC)
avg_past_medals = non_host_years.groupby('NOC')['Total_medals'].mean()

# Step 4: Merge avg_past_medals back into the original dataset
medals_df = medals_df.merge(avg_past_medals.rename('avg_past_medals'), on='NOC', how='left')

# Step 5: Save the updated dataset
medals_df.to_csv('medals_by_country.csv', index=False)
