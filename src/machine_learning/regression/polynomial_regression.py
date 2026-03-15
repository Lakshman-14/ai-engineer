import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Sample data (X, Y)
X = np.array([1, 2, 3, 4]).reshape(-1, 1)
y = np.array([1, 4, 9, 15])

# Step 1: Convert input to Polynomial Features (degree=2)
# creates: For input X = [x] it generates → [1, x, x²]
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Step 2: Fit the Regression Model
model = LinearRegression()
model.fit(X_poly, y)

# Step 3: Predict using the trained model
# predictions will be used to draw the regression curve.
y_pred = model.predict(X_poly)

# Step 4: Print coefficients
print("Intercept (b0)  =", model.intercept_)
print("Coefficients b1,b2 =", model.coef_)

# Step 5: Plotting
plt.scatter(X, y, color='blue', label='Original Data')
plt.plot(X, y_pred, color='red', label='Polynomial Fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Regression (Degree = 2)')
plt.legend()
plt.show()
