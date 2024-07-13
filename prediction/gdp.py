import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read the CSV file
df = pd.read_csv("canada_gdp.csv")

# Print the column names
print(df.columns)

# Plotting the data
plt.scatter(df['year'], df['per capita income (US$)'])
plt.xlabel('Year')
plt.ylabel('Per Capita Income (US$)')
plt.title('Per Capita Income Over Years')
plt.grid(True)
plt.show()

# Prepare the data for the linear regression model
X = df[['year']]  # Features (independent variable)
y = df['per capita income (US$)']  # Target (dependent variable)

# Create and fit the linear regression model
reg = LinearRegression()
reg.fit(X, y)

# Print the coefficients
print(f"Coefficient: {reg.coef_[0]}")
print(f"Intercept: {reg.intercept_}")

# Predicting values
y_pred = reg.predict(X)

# Plotting the regression line
plt.scatter(df['year'], df['per capita income (US$)'], color='blue')
plt.plot(df['year'], y_pred, color='red', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Per Capita Income (US$)')
plt.title('Per Capita Income Over Years with Regression Line')
plt.grid(True)
plt.show()

# Predicting the per capita income for the year 2020
year_2020 = np.array([[2020]])
income_2020 = reg.predict(year_2020)
print(f"Predicted per capita income for the year 2020: {income_2020[0]}")