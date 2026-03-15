import numpy as np
from sklearn.linear_model import Ridge

# -----------------------------
# 1. Sample numeric dataset
# -----------------------------
# We'll create a simple 1D dataset
X = np.array([ [1, 1], [1, 2], [1, 3]])  # adding bias term for intercept [bias, actual_feature]
y = np.array([1.2, 3.9, 9.1])     # target (roughly x^2 with noise)

# -----------------------------
# 2. Define Ridge model
# -----------------------------
alpha = 1.0        # Regularization strength (lambda also called λ)
model = Ridge(alpha=alpha, fit_intercept=False)

# -----------------------------
# 3. Fit the model
# -----------------------------
model.fit(X, y)

# -----------------------------
# 4. Print model parameters
# -----------------------------
print("--- Ridge Regression Model ---")
print(f"alpha (λ): {alpha}")
print(f"Coefficients: {model.coef_}")
print(f"Coefficient (b0/intercept): {model.coef_[0]:.4f}")
print(f"Coefficient (b1/slope): {model.coef_[1]:.4f}")

# -----------------------------
# 5. Make prediction
# -----------------------------
x_test = np.array([[1, 6]])  # bias term + x=6
y_pred = model.predict(x_test)

print(f"\nPredicted value for x=6: {y_pred[0]:.4f}")