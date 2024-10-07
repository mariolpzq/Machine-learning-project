import pandas as pd

df = pd.read_csv('olympics_dataset.csv')
# Assuming df is your DataFrame with the Olympic data
# Filter out rows with "No medal" since they are not needed
df_medals = df[df['Medal'] != 'No medal']

# Group by 'Team' and 'Year', and count each medal type
medal_counts = df_medals.groupby(['Team', 'Year', 'Medal']).size().unstack(fill_value=0)

# Rename columns for clarity
medal_counts.columns = ['Bronze', 'Gold', 'Silver']

# Reset the index to get 'Team' and 'Year' as columns
medal_counts = medal_counts.reset_index()

# Reorder columns if necessary (Team, Year, Gold, Silver, Bronze)
medal_counts = medal_counts[['Team', 'Year', 'Gold', 'Silver', 'Bronze']]

# If needed, save the result to a CSV file
medal_counts.to_csv('medal_counts.csv', index=False)

print(medal_counts)