import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read the CSV file
df = pd.read_excel("salary.xlsx")

# Print the column names
print(df.columns)

# Plotting the data
plt.scatter(df['year'], df['salary'])
plt.xlabel('Year')
plt.ylabel('salary')
plt.title('Income Over The Years')
plt.grid(True)
plt.show()

# Prepare the data for the linear regression model
X = df[['year']]  # Features (independent variable)
y = df['salary']  # Target (dependent variable)

# Create and fit the linear regression model
reg = LinearRegression()
reg.fit(X, y)

# Print the coefficients
print(f"Coefficient: {reg.coef_[0]}")
print(f"Intercept: {reg.intercept_}")

# Predicting values
y_pred = reg.predict(X)

# Plotting the regression line
plt.scatter(df['year'], df['salary'], color='blue')
plt.plot(df['year'], y_pred, color='red', linewidth=2)
plt.xlabel('Year')
plt.ylabel('salary')
plt.title('Income Over Years')
plt.grid(True)
plt.show()

# Predicting the income for the year 2020
year_2028 = np.array([[2028]])
income_2028 = reg.predict(year_2028)
print(f"Predicted  income for the year 2028: {income_2028[0]}")