# This script removes rows from the dataset where the 'Team' column has a number at the end of the team name (faulty rows)

import pandas as pd
import re # Import the regular expression module

medals_df = pd.read_csv('medals_by_country.csv')

def has_number_at_end(team_name):
    return bool(re.search(r'-\d+$', team_name))

medals_df = medals_df[~medals_df['Team'].apply(has_number_at_end)]
medals_df.to_csv('medals_by_country.csv', index=False)
