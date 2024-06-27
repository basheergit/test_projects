import pandas as pd

# Step 1: Read the initial CSV file and group by 'pc_name', summing 'total_votes'
df_initial = pd.read_csv('results_2014.csv')

# Group by 'pc_name' and sum the 'total_votes'
grouped = df_initial.groupby('pc_name')['total_votes'].sum().reset_index()

# Save the grouped data to a new CSV file
grouped.to_csv('2014_grouped_results.csv', index=False)

# Step 2: Read the grouped CSV file
df_grouped = pd.read_csv('2014_grouped_results.csv')

# Specify the column you want to get the bottom 5 values from
column_name = 'total_votes'

# Get the bottom 5 values in the specified column
bottom_5 = df_grouped.nsmallest(5, column_name)

# Print the bottom 5 values DataFrame
print("\nBottom 5 values in column '{}':".format(column_name))
print(bottom_5)

# Save the original grouped DataFrame and the bottom 5 values DataFrame into an Excel file with multiple sheets
with pd.ExcelWriter('2014_data_with_bottom_5.xlsx', engine='openpyxl') as writer:
    df_grouped.to_excel(writer, sheet_name='Original Data', index=False)
    bottom_5.to_excel(writer, sheet_name='Bottom 5 Values', index=False)

print("The bottom 5 values have been saved to '2014_data_with_bottom_5.xlsx' in a new sheet.")