import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('results_2014.csv')

# Clean and preprocess data if needed
# For example, remove leading/trailing spaces from 'candidate' column
df['candidate'] = df['candidate'].str.strip()

# Group by 'pc_name' and find top two highest 'total_votes' for each group
top_two_votes = df.groupby('pc_name', as_index=False).apply(lambda group: group.nlargest(2, 'total_votes')).reset_index(drop=True)

# Determine the winner (candidate with the highest total votes) and runner-up
winners = top_two_votes.groupby('pc_name').head(1).reset_index(drop=True)
runners = top_two_votes.groupby('pc_name').tail(1).reset_index(drop=True)

# Merge winners and runners back to top_two_votes to add the winner and runner information
top_two_votes = pd.merge(top_two_votes, winners[['pc_name', 'candidate', 'party', 'total_votes']], on='pc_name', suffixes=('', '_winner'))
top_two_votes = pd.merge(top_two_votes, runners[['pc_name', 'candidate', 'party', 'total_votes']], on='pc_name', suffixes=('', '_runner'))

# Calculate the difference in votes between winner and runner-up
top_two_votes['Vote Difference'] = top_two_votes['total_votes_winner'] - top_two_votes['total_votes_runner']

# Drop duplicates to ensure unique entries
top_two_votes.drop_duplicates(inplace=True)

# Sort by 'Vote Difference' column in descending order
top_two_votes.sort_values(by='Vote Difference', ascending=False, inplace=True)

# Select top 5 entries with highest 'Vote Difference'
top_5_highest_difference = top_two_votes.head(10)

# Print the top 5 entries with highest vote difference
print("Top 5 entries with highest Vote Difference:")
print(top_5_highest_difference[['pc_name', 'candidate_winner', 'party', 'total_votes_winner', 'candidate_runner', 'total_votes_runner', 'Vote Difference']])

# Create a new Excel workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = 'Top Two Highest Votes'

# Write the DataFrame to Excel
for r in dataframe_to_rows(top_5_highest_difference, index=False, header=True):
    ws.append(r)

# Save the workbook
excel_output_path = '2014_top_5_winner.xlsx'
wb.save(excel_output_path)

print(f"Top 5 entries with highest vote difference saved to {excel_output_path}")
