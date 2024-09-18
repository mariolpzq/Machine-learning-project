import pandas as pd

# Load the datasets
olympics_df = pd.read_csv('olympics_dataset.csv')
medals_df = pd.read_csv('medals_by_country.csv')

# Step 1: Calculate the number of unique events each country participated in per year
events_per_country_year = olympics_df.groupby(['Team', 'Year'])['Event'].nunique().reset_index()
events_per_country_year.rename(columns={'Event': 'Number of events'}, inplace=True)

# Step 2: Merge the "Number of events" column into medals_by_country.csv
medals_df = pd.merge(medals_df, events_per_country_year, on=['Team', 'Year'], how='left')

# Step 3: Save the updated medals_by_country.csv
medals_df.to_csv('medals_by_country.csv', index=False)
