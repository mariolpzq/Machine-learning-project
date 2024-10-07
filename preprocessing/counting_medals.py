# This script calculates the number of medals won by each country in each year, 
# as well as the number of athletes representing each country in each year
import pandas as pd

df = pd.read_csv('olympics_dataset.csv')

df_medals = df[df['Medal'] != 'No medal']
df_unique_medals = df_medals.drop_duplicates(subset=['Team', 'Year', 'Sport', 'Event', 'Medal'])

medal_counts = df_unique_medals.groupby(['Team', 'Year', 'Medal']).size().unstack(fill_value=0)
medal_counts.columns = ['Bronze', 'Gold', 'Silver']
medal_counts = medal_counts.reset_index()

athlete_counts = df.groupby(['Team', 'Year'])['Name'].nunique().reset_index()
athlete_counts.columns = ['Team', 'Year', 'Number of Athletes']

result = pd.merge(medal_counts, athlete_counts, on=['Team', 'Year'], how='left')
result = result[['Team', 'Year', 'Gold', 'Silver', 'Bronze', 'Number of Athletes']]
result.to_csv('medal_and_athlete_counts3.csv', index=False)
