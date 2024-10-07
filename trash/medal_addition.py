import pandas as pd

# Load the dataset
df = pd.read_csv('medals_by_country.csv')

# List of teams to analyze
teams = [
    'Australia', 'Brazil', 'China', 'France', 'Great Britain',
    'Japan', 'South Korea', 'Spain', 'United States'
]

# Filter the dataset for the specified teams
filtered_df = df[df['Team'].isin(teams)]

# Calculate the total number of medals for each team when they were hosts and not hosts
results = {}
for team in teams:
    team_data = filtered_df[filtered_df['Team'] == team]
    total_medals_host = team_data[team_data['isHost'] == 1]['Total_medals'].sum()
    total_medals_non_host = team_data[team_data['isHost'] == 0]['Total_medals'].sum()
    results[team] = {
        'Total Medals (Host)': total_medals_host,
        'Total Medals (Non-Host)': total_medals_non_host
    }

# Print the results
for team, medal_counts in results.items():
    print(f"Team: {team}")
    print(f"  Total Medals when Host: {medal_counts['Total Medals (Host)']}")
    print(f"  Total Medals when Non-Host: {medal_counts['Total Medals (Non-Host)']}")
    print()
