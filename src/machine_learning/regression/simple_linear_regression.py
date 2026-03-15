# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample dataset
# Using values: X [1, 2, 3, 4, 5], Y [2, 4, 5, 4, 5]
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Feature
y = np.array([2, 4, 5, 4, 5])                 # Target

# Step 1: Train-Test Split (80-20 ratio)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 2: Create the Linear Regression model
model = LinearRegression()

# Step 3: Train the model
model.fit(X_train, y_train)

# Step 4: Display model parameters
print("\nIntercept (b0):", model.intercept_)
print("\nCoefficient (b1):", model.coef_[0])

# Step 5: Evaluate the model on test data
y_pred = model.predict(X_test)

print("\nTest Data X:", X_test.flatten())
print("\nActual y:", y_test)
print("\nPredicted y:", y_pred)

# Performance Metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nMean Squared Error: {mse:.2f}")
print(f"\nR² Score: {r2:.2f}")

# Visualization
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Model')
plt.legend()
plt.show()
