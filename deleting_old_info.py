import pandas as pd

file_path = 'olympics_dataset.csv'
df = pd.read_csv(file_path)

# Filter rows where "Year" is greater than or equal to 1984
filtered_df = df[df['Year'] >= 1984]

filtered_df.to_csv(file_path, index=False)

print("Rows with 'Year' less than 1984 have been deleted.")