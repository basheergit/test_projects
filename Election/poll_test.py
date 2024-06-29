import pandas as pd

# Read the CSV file
df_initial = pd.read_csv('results_2014.csv', low_memory=False)

# Print the columns to identify the correct column name
print("Columns in the DataFrame:", df_initial.columns)

# Convert the 'voter_turnout_ratio' column to numeric, forcing errors to NaN
df_initial['voter_turnout_ratio'] = pd.to_numeric(df_initial['voter_turnout_ratio'], errors='coerce')

# Print the data types to verify conversion
print("Data types after conversion:\n", df_initial.dtypes)

# Drop rows with NaN values in 'voter_turnout_ratio' if necessary
df_initial = df_initial.dropna(subset=['voter_turnout_ratio'])

# Ensure the column is of numeric type
df_initial['voter_turnout_ratio'] = df_initial['voter_turnout_ratio'].astype(float)

# Print the data types again to confirm
print("Data types after ensuring float:\n", df_initial.dtypes)

# Replace 'some_column' with the actual column name you want to group by
group_column = 'state'  # Replace this with the correct column name

# Select only numeric columns for aggregation
numeric_columns = df_initial.select_dtypes(include='number').columns

# Print the numeric columns to verify
print("Numeric columns for aggregation:", numeric_columns)

# Group by the desired column and calculate the mean for numeric columns only
df_grouped = df_initial.groupby(group_column)[numeric_columns].mean()

# Get the bottom 5 rows based on 'voter_turnout_ratio'
bottom_5 = df_grouped.nsmallest(5, 'voter_turnout_ratio')

print(bottom_5)