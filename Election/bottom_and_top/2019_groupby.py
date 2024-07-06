import pandas as pd

# Sample DataFrame
df = pd.read_csv('results_2019.csv')

# Group by 'pc_name' and count the number of voters
grouped = df.groupby('pc_name')['total_votes'].sum().reset_index()

# Save the grouped data to a new CSV file
grouped.to_csv('2019_grouped_results.csv', index=False)