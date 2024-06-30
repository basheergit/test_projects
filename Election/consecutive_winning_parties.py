import pandas as pd

# Read the 2019 CSV file
df_2019 = pd.read_csv('results_2019.csv')

# Group by 'state', 'pc_name', and 'party', then sum the 'total_votes'
grouped_2019 = df_2019.groupby(['state', 'pc_name', 'party'])['total_votes'].sum().reset_index()

# Find the party with the highest votes in each 'pc_name'
idx_2019 = grouped_2019.groupby('pc_name')['total_votes'].idxmax()
result_2019 = grouped_2019.loc[idx_2019]

# Save the result to an Excel file
result_2019.to_excel('2019_party_with_highest_votes.xlsx', index=False)
print("The result has been saved to '2019_party_with_highest_votes.xlsx'")

# Read the 2014 CSV file
df_2014 = pd.read_csv('results_2014.csv')

# Group by 'state', 'pc_name', and 'party', then sum the 'total_votes'
grouped_2014 = df_2014.groupby(['state', 'pc_name', 'party'])['total_votes'].sum().reset_index()

# Find the party with the highest votes in each 'pc_name'
idx_2014 = grouped_2014.groupby('pc_name')['total_votes'].idxmax()
result_2014 = grouped_2014.loc[idx_2014]

# Save the result to an Excel file
result_2014.to_excel('2014_party_with_highest_votes.xlsx', index=False)
print("The result has been saved to '2014_party_with_highest_votes.xlsx'")

# Load the 2014 and 2019 Excel files into DataFrames
df_2014 = pd.read_excel('2014_party_with_highest_votes.xlsx')
df_2019 = pd.read_excel('2019_party_with_highest_votes.xlsx')

# Check if the necessary columns exist in the DataFrames
required_columns = ['state', 'pc_name', 'party', 'total_votes']
for col in required_columns:
    if col not in df_2014.columns:
        raise KeyError(f"Column '{col}' not found in the 2014 DataFrame")
    if col not in df_2019.columns:
        raise KeyError(f"Column '{col}' not found in the 2019 DataFrame")

# Merge the DataFrames on 'state', 'pc_name', and 'party'
consecutive_winning_parties = pd.merge(df_2014, df_2019, on=['state', 'pc_name', 'party'], suffixes=('_2014', '_2019'))

# Select the relevant columns
result = consecutive_winning_parties[['state', 'pc_name', 'party', 'total_votes_2014', 'total_votes_2019']]

# Save the result to a new Excel file
result.to_excel('consecutive_winning_parties.xlsx', index=False)
print("The consecutive winning parties have been saved to 'consecutive_winning_parties.xlsx'")