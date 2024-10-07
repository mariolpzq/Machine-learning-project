# This script adds a new column to the dataset that indicates whether the country is the host country or not

import pandas as pd

medals_df = pd.read_csv('medals_by_country.csv')
medals_df['isHost'] = (medals_df['NOC'] == medals_df['Host country']).astype(int)
medals_df.to_csv('medals_by_country.csv', index=False)
