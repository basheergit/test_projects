import pandas as pd
import os

# Sample DataFrame
df = pd.read_csv('results_2014.csv')

# Group by 'state' and sum the 'total_electors'
grouped = df.groupby('state')['total_electors'].sum().reset_index()

# Save the grouped data to a new CSV file
grouped.to_csv('2014_state_with_electrols_grouped_results.csv', index=False)

df5 = pd.read_csv('results_2014.csv')
# Group by 'pc_name' and count the number of voters
grouped = df5.groupby('state')['total_votes'].sum().reset_index()

# Save the grouped data to a new CSV file
grouped.to_csv('2014_state_grouped_results.csv', index=False)

# Read the CSV files into DataFrames
df1 = pd.read_csv('2014_state_with_electrols_grouped_results.csv')
df2 = pd.read_csv('2014_state_grouped_results.csv')

# Merge the DataFrames on the common column 'state'
merged_df = pd.merge(df1, df2, on='state')

# Display the merged DataFrame
print(merged_df)

# Optionally, save the merged DataFrame to a new CSV file
merged_df.to_csv('2014_state_merged_file.csv', index=False)

# Read the CSV file into a DataFrame
df3 = pd.read_csv('2014_state_merged_file.csv')

# Ensure 'total_votes' and 'total_electors' columns exist in df3
if 'total_votes' in df3.columns and 'total_electors' in df3.columns:
    # Create a new column 'voter_turnout_ratio' which is the ratio of 'total_votes' to 'total_electors'
    df3['voter_turnout_ratio'] = df3['total_votes'] / df3['total_electors']
else:
    raise ValueError("Columns 'total_votes' and/or 'total_electors' are missing in the DataFrame")

# Define the name of the Excel file and the new sheet name
excel_file = '2014_state_merged_file.xlsx'
new_sheet_name = 'voter_turnout_ratio'

# Display the DataFrame with the new column
print(df3)

# Check if the Excel file exists
if not os.path.exists(excel_file):
    # Create the Excel file with an initial sheet
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        df3.to_excel(writer, sheet_name='InitialSheet', index=False)

# Write the DataFrame to a new sheet in the Excel file, replacing the sheet if it already exists
with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df3.to_excel(writer, sheet_name=new_sheet_name, index=False)

print(f"DataFrame with ratio column added to sheet '{new_sheet_name}' in '{excel_file}'")

# Read the specific sheet from the Excel file into a DataFrame
df4 = pd.read_excel(excel_file, sheet_name=new_sheet_name)

# Specify the column you want to get the bottom 5 values from
column_name = 'voter_turnout_ratio'

# Get the bottom 5 values in the specified column
bottom_5 = df4.nsmallest(5, column_name)

# Print the bottom 5 values DataFrame
print("\nBottom 5 values in column '{}':".format(column_name))
print(bottom_5)

# Sort the DataFrame by the column of interest in descending order and get the top 5 values
top_5 = df4.nlargest(5, column_name)

# Print the top 5 values DataFrame
print("\nTop 5 values in column '{}':".format(column_name))
print(top_5)

# Save the original DataFrame, the bottom 5 values DataFrame, and the top 5 values DataFrame into an Excel file with multiple sheets
with pd.ExcelWriter('2014_data_with_bottom_top_5.xlsx', engine='openpyxl') as writer:
    df4.to_excel(writer, sheet_name='Original Data', index=False)
    bottom_5.to_excel(writer, sheet_name='Bottom 5 Values', index=False)
    top_5.to_excel(writer, sheet_name='Top 5 Values', index=False)

print("The bottom 5 and top 5 values have been saved to '2014_data_with_bottom_top_5.xlsx' in new sheets.")