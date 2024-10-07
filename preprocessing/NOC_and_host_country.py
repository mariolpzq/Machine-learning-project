# This script maps NOC codes and Host countries
import pandas as pd

medals_df = pd.read_csv('medals_by_country.csv')
olympics_df = pd.read_csv('olympics_dataset.csv')

noc_mapping = olympics_df[['Team', 'NOC']].drop_duplicates()
noc_mapping = noc_mapping.set_index('Team')['NOC'].to_dict()

host_mapping = olympics_df[['Year', 'Host country']].drop_duplicates()
host_mapping = host_mapping.set_index('Year')['Host country'].to_dict()


medals_df['NOC'] = medals_df['Team'].map(noc_mapping)
medals_df['Host country'] = medals_df['Year'].map(host_mapping)

medals_df.to_csv('updated_medals_my_country.csv', index=False)
