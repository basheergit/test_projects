import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('2019_grouped_results.csv')

# Specify the column you want to get the bottom 5 values from
column_name = 'total_votes'

# Get the bottom 5 values in the specified column
bottom_5 = df.nsmallest(5, column_name)


# Print the bottom 5 values DataFrame
print("\nBottom 5 values in column '{}':".format(column_name))
print(bottom_5)

# Save the original DataFrame and the bottom 5 values DataFrame into an Excel file with multiple sheets
with pd.ExcelWriter('2019_data_with_bottom_5.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Original Data', index=False)
    bottom_5.to_excel(writer, sheet_name='Bottom 5 Values', index=False)
    
print("The bottom 5 values have been saved to '2019_data_with_bottom_5.xlsx' in a new sheet.")

