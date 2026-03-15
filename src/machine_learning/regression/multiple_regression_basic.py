# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load Dataset
data = pd.DataFrame({
    'x1': [1, 2, 3],
    'x2': [2, 1, 4],
    'Output': [6, 8, 14]
})

# 2. Feature & Label Separation
X = data[['x1', 'x2']]
y = data['Output']

# 3. Train/Test Split (using same data because dataset is tiny)
X_train, X_test = X, X
y_train, y_test = y, y

# 4. Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Performance Evaluation
y_pred = model.predict(X_test)

print("\n--- Model Coefficients ---")
print("Intercept (β0):", model.intercept_)
print("Coefficients (β1, β2):", model.coef_)

print("\n--- Model Performance Evaluation ---")
print("Predicted values:", y_pred)
print("Actual values:", y_test.values)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
print(f"R² Score: {r2_score(y_test, y_pred):.2f}")

# 6. Graph Plotting (3D Regression Plane)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot actual data points
ax.scatter(X_test['x1'], X_test['x2'], y_test, color='blue', s=100, label='Actual Data Points')

# Create a meshgrid for plotting regression plane
x1_surf = np.linspace(X['x1'].min(), X['x1'].max(), 10)
x2_surf = np.linspace(X['x2'].min(), X['x2'].max(), 10)
x1_surf, x2_surf = np.meshgrid(x1_surf, x2_surf)

# Predict y values for the meshgrid
y_plane = model.predict(pd.DataFrame({
    'x1': x1_surf.ravel(),
    'x2': x2_surf.ravel()
}))
y_plane = y_plane.reshape(x1_surf.shape)

# Plot regression plane
ax.plot_surface(x1_surf, x2_surf, y_plane, color='red', alpha=0.3, label="Regression Plane")

# Labels & Title
ax.set_xlabel('x1 (Input Feature 1)')
ax.set_ylabel('x2 (Input Feature 2)')
ax.set_zlabel('Output (Prediction)')
ax.set_title('3D Multiple Linear Regression Plane')
ax.legend()

plt.show()
