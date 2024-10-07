import pandas as pd

# Load the dataset
df = pd.read_csv('medals_by_country.csv')

# Define the specific team and year
team = 'United States'
year_host = 1996

# Filter the dataset for the United States
us_data = df[(df['Team'] == team) & (df['Year'] == year_host)]

# Calculate the total number of medals for the US when they hosted in 1996
total_medals_host = us_data[us_data['isHost'] == 1]['Total_medals'].sum()
total_medals_non_host = us_data[us_data['isHost'] == 0]['Total_medals'].sum()

# Print the results
print(f"Team: {team}")
print(f"  Total Medals when Host in {year_host}: {total_medals_host}")
print(f"  Total Medals when Non-Host in {year_host}: {total_medals_non_host}")
