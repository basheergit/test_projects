import pandas as pd

# Step 1: Read the initial CSV file and group by 'pc_name', summing 'voter_turnout_ratio'
df_initial = pd.read_csv('results_2014.csv')

# Group by 'pc_name' and sum the 'voter_turnout_ratio'
grouped = df_initial.groupby('pc_name')['voter_turnout_ratio'].sum().reset_index()

# Save the grouped data to a new CSV file
grouped.to_csv('2014_grouped_results.csv', index=False)

# Step 2: Read the grouped CSV file
df_grouped = pd.read_csv('2014_grouped_results.csv')

# Specify the column you want to get the bottom 5 values from
column_name = 'voter_turnout_ratio'

# Get the bottom 5 values in the specified column
bottom_5 = df_grouped.nsmallest(5, column_name)

# Print the bottom 5 values DataFrame
print("\nBottom 5 values in column '{}':".format(column_name))
print(bottom_5)

# Sort the DataFrame by the column of interest in descending order and get the top 5 values
top_5 = df_grouped.nlargest(5, column_name)


# Print the top 5 values DataFrame
print("\ntop 5 values in column '{}':".format(column_name))
print(top_5)



# Save the original grouped DataFrame and the bottom 5 values DataFrame into an Excel file with multiple sheets
with pd.ExcelWriter('2014_data_with_bottom_5.xlsx', engine='openpyxl') as writer:
    df_grouped.to_excel(writer, sheet_name='Original Data', index=False)
    bottom_5.to_excel(writer, sheet_name='Bottom 5 Values', index=False)

with pd.ExcelWriter('2014_data_with_top_5.xlsx', engine='openpyxl') as writer:
    df_grouped.to_excel(writer, sheet_name='Original Data', index=False)
    top_5.to_excel(writer, sheet_name='top 5 Values', index=False)
    
print("The top & bottom 5 values have been saved to '2014_data_with_top_5.xlsx' in a new sheets.")


