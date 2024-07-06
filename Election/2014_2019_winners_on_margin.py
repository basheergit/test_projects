import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Read the CSV files into pandas DataFrames
df_2014 = pd.read_csv('results_2014.csv')
df_2019 = pd.read_csv('results_2019.csv')

# Clean and preprocess data if needed
df_2014['candidate'] = df_2014['candidate'].str.strip()
df_2019['candidate'] = df_2019['candidate'].str.strip()

# Function to process and get top two votes
def get_top_two(df):
    top_two_votes = df.groupby('pc_name', as_index=False).apply(lambda group: group.nlargest(2, 'total_votes')).reset_index(drop=True)
    winners = top_two_votes.groupby('pc_name').head(1).reset_index(drop=True)
    runners = top_two_votes.groupby('pc_name').tail(1).reset_index(drop=True)
    top_two_votes = pd.merge(top_two_votes, winners[['pc_name', 'candidate', 'party', 'total_votes']], on='pc_name', suffixes=('', '_winner'))
    top_two_votes = pd.merge(top_two_votes, runners[['pc_name', 'candidate', 'party', 'total_votes']], on='pc_name', suffixes=('', '_runner'))
    top_two_votes['Vote Difference'] = top_two_votes['total_votes_winner'] - top_two_votes['total_votes_runner']
    top_two_votes.drop_duplicates(inplace=True)
    top_two_votes.sort_values(by='Vote Difference', ascending=False, inplace=True)
    return top_two_votes.head(10)  # Adjust as needed for top entries

# Get top 5 entries for both 2014 and 2019
top_5_2014 = get_top_two(df_2014)
top_5_2019 = get_top_two(df_2019)

# Create a new Excel workbook
wb = Workbook()

# Create sheets for 2014 and 2019 results
ws_2014 = wb.active
ws_2014.title = 'Top Two 2014'
ws_2019 = wb.create_sheet(title='Top Two 2019')

# Write 2014 data to the first sheet
for r in dataframe_to_rows(top_5_2014, index=False, header=True):
    ws_2014.append(r)

# Write 2019 data to the second sheet
for r in dataframe_to_rows(top_5_2019, index=False, header=True):
    ws_2019.append(r)

# Save the workbook
excel_output_path = '2014_2019_top_5_winners.xlsx'
wb.save(excel_output_path)

print(f"Top 5 entries with highest vote difference for 2014 and 2019 saved to {excel_output_path}")
