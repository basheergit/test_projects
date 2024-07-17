import pandas as pd
import numpy as np
from sklearn import linear_model
import math

# Load the dataset
df = pd.read_csv("homeprices.csv")

# Calculate the median of the 'bedrooms' column and floor it
median_bedrooms = math.floor(df.bedrooms.median())
print("Median Bedrooms (floored):", median_bedrooms)

# Fill NaN values in 'bedrooms' column with the median value
df.bedrooms = df.bedrooms.fillna(median_bedrooms)
print("DataFrame after filling NaN values in 'bedrooms':\n", df)

# Create and train the linear regression model
reg = linear_model.LinearRegression()
reg.fit(df[['area', 'bedrooms', 'age']], df.price)

# Print the coefficients and intercept of the model
print("Coefficients:", reg.coef_)
print("Intercept:", reg.intercept_)

# Prepare the input data for prediction
input_data = pd.DataFrame([[3000, 3, 4]], columns=['area', 'bedrooms', 'age'])

# Make a prediction
prediction = reg.predict(input_data)
print("Prediction for input [3000, 3, 4]:", prediction)