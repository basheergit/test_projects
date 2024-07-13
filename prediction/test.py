import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Step 1: Load the data
data = pd.read_csv('canada_gdp.csv')

# Step 2: Preprocess the data
# Assuming the CSV has columns: 'Year', 'Population', 'Investment', 'Exports', 'GDP'
# We will use 'per capita income (US$)' as the feature to predict 'year'

# Select features and target variable
X = data[['per capita income (US$)']]
y = data['year']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Build and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Make predictions
y_pred = model.predict(X_test)

# Step 5: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Optional: Print model coefficients
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)

# Example prediction
example_data = pd.DataFrame({
  'per capita income (US$)': [3399.299037],    
})
predicted_year = model.predict(example_data)
print(f'Predicted Year: {predicted_year[0]}')

# Step 6: Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', edgecolor='k', alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.xlabel('Actual Year')
plt.ylabel('Predicted Year')
plt.title('Actual vs Predicted Year')
plt.grid(True)
plt.show()