import pandas as pd
import numpy as np
from sklearn import linear_model
import math

# Load the dataset
df = pd.read_csv("hiring.csv")

# Dictionary to map number names to numerical values
number_mapping = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9,
  'ten': 10
}

# Function to convert number names to numbers
def convert_number_name_to_number(name):
  return number_mapping.get(name, None)  # Returns None if the name is not found

# Apply the conversion function to the 'experience' column
df['experience'] = df['experience'].apply(convert_number_name_to_number)

# Handle missing values (if any)
df['experience'].fillna(0, inplace=True)
df['test_score'].fillna(df['test_score'].mean(), inplace=True)
df['interview_score'].fillna(df['interview_score'].mean(), inplace=True)

print(df)

# Create and train the linear regression model
reg = linear_model.LinearRegression()
reg.fit(df[['experience', 'test_score', 'interview_score']], df['salary'])

# Print the coefficients and intercept of the model
print("Coefficients:", reg.coef_)
print("Intercept:", reg.intercept_)

# Prepare the input data for prediction
input_data = pd.DataFrame([[8, 8, 9]], columns=['experience', 'test_score', 'interview_score'])

# Make a prediction
prediction = reg.predict(input_data)
print("Prediction for input [8, 8, 9]:", prediction)