# This script deletes all the information before 1984

import pandas as pd

file_path = 'olympics_dataset.csv'
df = pd.read_csv(file_path)

filtered_df = df[df['Year'] >= 1984]
filtered_df.to_csv(file_path, index=False)
