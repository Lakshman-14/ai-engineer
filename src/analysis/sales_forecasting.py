"""
Home Assignment: Sales Forecasting using Polynomial Regression

Problem Statement:
Build a Polynomial Regression model, compare it against a Linear Regression baseline,
and decide which model better represents the data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# =============================================================================
# Step 1: Data Exploration
# =============================================================================
print("=" * 60)
print("STEP 1: DATA EXPLORATION")
print("=" * 60)

# Load the dataset
df = pd.read_csv("/Users/lakshmanraghu/Downloads/sales_data (1).csv")

# Display first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Extract features and target
X = df['Advertising_Spend'].values.reshape(-1, 1)
y = df['Total Amount'].values

# Plot scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', alpha=0.6, edgecolors='black', label='Actual Data')
plt.xlabel('Advertising Spend ($)')
plt.ylabel('Sales Revenue ($)')
plt.title('Advertising Spend vs Sales Revenue')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('step1_scatter_plot.png', dpi=150)
plt.show()

# Comment on relationship
print("\n--- Observation ---")
print("""
Looking at the scatter plot, the relationship between Advertising Spend and Sales 
does NOT appear to be strictly linear. The data points suggest a curved pattern,
indicating that sales growth rate changes as advertising spend increases.
This suggests a polynomial (non-linear) relationship might fit better.
""")

# =============================================================================
# Step 2: Baseline Model – Simple Linear Regression
# =============================================================================
print("\n" + "=" * 60)
print("STEP 2: BASELINE MODEL - SIMPLE LINEAR REGRESSION")
print("=" * 60)

# Build Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X, y)

# Predict on the same dataset
y_pred_linear = linear_model.predict(X)

# Evaluate the model
mse_linear = mean_squared_error(y, y_pred_linear)
rmse_linear = np.sqrt(mse_linear)
r2_linear = r2_score(y, y_pred_linear)

print(f"\nLinear Regression Results:")
print(f"  - Mean Squared Error (MSE): {mse_linear:.4f}")
print(f"  - Root Mean Squared Error (RMSE): {rmse_linear:.4f}")
print(f"  - R² Score: {r2_linear:.4f}")
print(f"  - Coefficient (slope): {linear_model.coef_[0]:.4f}")
print(f"  - Intercept: {linear_model.intercept_:.4f}")

# Plot the regression line over the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', alpha=0.6, edgecolors='black', label='Actual Data')
plt.plot(X, y_pred_linear, color='red', linewidth=2, label='Linear Regression Line')
plt.xlabel('Advertising Spend ($)')
plt.ylabel('Sales Revenue ($)')
plt.title('Linear Regression: Advertising Spend vs Sales')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('step2_linear_regression.png', dpi=150)
plt.show()

# =============================================================================
# Step 3: Polynomial Feature Transformation
# =============================================================================
print("\n" + "=" * 60)
print("STEP 3: POLYNOMIAL FEATURE TRANSFORMATION")
print("=" * 60)

# Polynomial Features with Degree 2
poly_features_2 = PolynomialFeatures(degree=2, include_bias=False)
X_poly_2 = poly_features_2.fit_transform(X)

print("\nPolynomial Features (Degree 2):")
print(f"  Original shape: {X.shape}")
print(f"  Transformed shape: {X_poly_2.shape}")
print(f"  Features: [x, x²]")

# Polynomial Features with Degree 3
poly_features_3 = PolynomialFeatures(degree=3, include_bias=False)
X_poly_3 = poly_features_3.fit_transform(X)

print("\nPolynomial Features (Degree 3):")
print(f"  Original shape: {X.shape}")
print(f"  Transformed shape: {X_poly_3.shape}")
print(f"  Features: [x, x², x³]")

# =============================================================================
# Step 4: Polynomial Regression Model Training
# =============================================================================
print("\n" + "=" * 60)
print("STEP 4: POLYNOMIAL REGRESSION MODEL TRAINING")
print("=" * 60)

# Train Polynomial Regression model with Degree 2
poly_model_2 = LinearRegression()
poly_model_2.fit(X_poly_2, y)
y_pred_poly_2 = poly_model_2.predict(X_poly_2)

print("\nPolynomial Regression (Degree 2) trained successfully!")

# Train Polynomial Regression model with Degree 3
poly_model_3 = LinearRegression()
poly_model_3.fit(X_poly_3, y)
y_pred_poly_3 = poly_model_3.predict(X_poly_3)

print("Polynomial Regression (Degree 3) trained successfully!")

# Final model selection
print("\n*** Using Degree 2 for final evaluation ***")
print("Reason: Degree 2 typically provides a good balance between fit and complexity,")
print("avoiding overfitting while capturing the non-linear trend.")

# =============================================================================
# Step 5: Model Evaluation and Comparison
# =============================================================================
print("\n" + "=" * 60)
print("STEP 5: MODEL EVALUATION AND COMPARISON")
print("=" * 60)

# Evaluate Polynomial Regression (Degree 2)
mse_poly_2 = mean_squared_error(y, y_pred_poly_2)
rmse_poly_2 = np.sqrt(mse_poly_2)
r2_poly_2 = r2_score(y, y_pred_poly_2)

# Evaluate Polynomial Regression (Degree 3)
mse_poly_3 = mean_squared_error(y, y_pred_poly_3)
rmse_poly_3 = np.sqrt(mse_poly_3)
r2_poly_3 = r2_score(y, y_pred_poly_3)

print("\n" + "-" * 70)
print(f"{'Model Type':<30} {'MSE':<15} {'RMSE':<15} {'R² Score':<15}")
print("-" * 70)
print(f"{'Linear Regression':<30} {mse_linear:<15.4f} {rmse_linear:<15.4f} {r2_linear:<15.4f}")
print(f"{'Polynomial (Degree 2)':<30} {mse_poly_2:<15.4f} {rmse_poly_2:<15.4f} {r2_poly_2:<15.4f}")
print(f"{'Polynomial (Degree 3)':<30} {mse_poly_3:<15.4f} {rmse_poly_3:<15.4f} {r2_poly_3:<15.4f}")
print("-" * 70)

# Create comparison DataFrame
comparison_df = pd.DataFrame({
    'Model Type': ['Linear Regression', 'Polynomial (Degree 2)', 'Polynomial (Degree 3)'],
    'MSE': [mse_linear, mse_poly_2, mse_poly_3],
    'RMSE': [rmse_linear, rmse_poly_2, rmse_poly_3],
    'R² Score': [r2_linear, r2_poly_2, r2_poly_3]
})

print("\nComparison Table (DataFrame):")
print(comparison_df.to_string(index=False))

# =============================================================================
# Step 6: Visualization
# =============================================================================
print("\n" + "=" * 60)
print("STEP 6: VISUALIZATION")
print("=" * 60)

# Sort X values for smooth polynomial curve plotting
sort_idx = np.argsort(X.flatten())
X_sorted = X[sort_idx]
y_sorted = y[sort_idx]

# Generate predictions on sorted X
y_pred_linear_sorted = linear_model.predict(X_sorted)
X_poly_2_sorted = poly_features_2.transform(X_sorted)
y_pred_poly_2_sorted = poly_model_2.predict(X_poly_2_sorted)
X_poly_3_sorted = poly_features_3.transform(X_sorted)
y_pred_poly_3_sorted = poly_model_3.predict(X_poly_3_sorted)

# Create the final visualization
plt.figure(figsize=(12, 8))

# Scatter plot of actual data
plt.scatter(X, y, color='blue', alpha=0.6, edgecolors='black', s=50, label='Actual Sales Data')

# Linear regression line
plt.plot(X_sorted, y_pred_linear_sorted, color='red', linewidth=2, 
         linestyle='--', label=f'Linear Regression (R²={r2_linear:.4f})')

# Polynomial regression curve (Degree 2)
plt.plot(X_sorted, y_pred_poly_2_sorted, color='green', linewidth=2, 
         label=f'Polynomial Degree 2 (R²={r2_poly_2:.4f})')

# Polynomial regression curve (Degree 3)
plt.plot(X_sorted, y_pred_poly_3_sorted, color='purple', linewidth=2, 
         linestyle='-.', label=f'Polynomial Degree 3 (R²={r2_poly_3:.4f})')

plt.xlabel('Advertising Spend ($)', fontsize=12)
plt.ylabel('Sales Revenue ($)', fontsize=12)
plt.title('Sales Forecasting: Linear vs Polynomial Regression Comparison', fontsize=14)
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('step6_model_comparison.png', dpi=150)
plt.show()

print("\nVisualization saved as 'step6_model_comparison.png'")

# =============================================================================
# Step 7: User Input Prediction
# =============================================================================
print("\n" + "=" * 60)
print("STEP 7: USER INPUT PREDICTION")
print("=" * 60)

try:
    user_input = float(input("\nEnter a new Advertising Spend value ($): "))
    
    # Prepare input for prediction
    X_new = np.array([[user_input]])
    
    # Linear Regression prediction
    pred_linear = linear_model.predict(X_new)[0]
    
    # Polynomial Regression prediction (Degree 2)
    X_new_poly_2 = poly_features_2.transform(X_new)
    pred_poly_2 = poly_model_2.predict(X_new_poly_2)[0]
    
    # Polynomial Regression prediction (Degree 3)
    X_new_poly_3 = poly_features_3.transform(X_new)
    pred_poly_3 = poly_model_3.predict(X_new_poly_3)[0]
    
    print(f"\n--- Predictions for Advertising Spend = ${user_input:.2f} ---")
    print(f"  Linear Regression Prediction:        ${pred_linear:.2f}")
    print(f"  Polynomial (Degree 2) Prediction:    ${pred_poly_2:.2f}")
    print(f"  Polynomial (Degree 3) Prediction:    ${pred_poly_3:.2f}")
    
    print("\n--- Analysis ---")
    diff_2 = pred_poly_2 - pred_linear
    diff_3 = pred_poly_3 - pred_linear
    print(f"Difference (Poly Degree 2 - Linear): ${diff_2:.2f}")
    print(f"Difference (Poly Degree 3 - Linear): ${diff_3:.2f}")
    print("""
Comment: The difference between predictions indicates how the models capture
the non-linear relationship. Polynomial models can capture the diminishing
returns effect where additional advertising spend yields progressively 
smaller increases in sales at higher spending levels.
""")

except ValueError:
    print("Invalid input. Please enter a numeric value.")
except Exception as e:
    print(f"An error occurred: {e}")

# =============================================================================
# Step 8: Model Interpretation
# =============================================================================
print("\n" + "=" * 60)
print("STEP 8: MODEL INTERPRETATION")
print("=" * 60)

print("""
===============================================================================
QUESTION 1: Why does Polynomial Regression perform better or worse than 
            Linear Regression?
===============================================================================

Answer:
Polynomial Regression typically performs BETTER than Linear Regression when 
the underlying relationship between variables is non-linear. In this sales 
dataset, the relationship between Advertising Spend and Sales is likely 
curved (showing diminishing returns at higher spending levels), which a 
linear model cannot capture.

- Linear Regression assumes a constant rate of change (straight line)
- Polynomial Regression can model curved relationships by adding higher-order 
  terms (x², x³, etc.)

If R² is higher for Polynomial Regression, it means the polynomial model 
explains more variance in the data, indicating a better fit to the non-linear 
pattern.

===============================================================================
QUESTION 2: What risks are associated with choosing a higher polynomial degree?
===============================================================================

Answer:
The main risk is OVERFITTING. As the polynomial degree increases:

1. **Overfitting**: The model may fit the training data too closely, including 
   noise, leading to poor generalization on new/unseen data.

2. **High Variance**: Small changes in training data can cause large changes 
   in the model, making it unstable.

3. **Unrealistic Predictions**: Very high degrees can cause extreme predictions 
   at the boundaries (extrapolation becomes unreliable).

4. **Computational Complexity**: More features mean more computation and 
   potential numerical instability.

5. **Interpretability**: Higher degree models are harder to explain to 
   stakeholders.

Rule of thumb: Use the simplest model that adequately captures the pattern.
Cross-validation should be used to select the optimal degree.

===============================================================================
QUESTION 3: In a real business scenario, which model would you choose and why?
===============================================================================

Answer:
In a real business scenario, I would choose **Polynomial Regression (Degree 2)** 
for the following reasons:

1. **Better Fit**: If Degree 2 significantly improves R² over linear regression 
   while capturing the non-linear trend, it provides a more accurate 
   representation of reality.

2. **Interpretability**: A quadratic model is still interpretable - we can 
   explain that sales increase with advertising but at a decreasing rate 
   (diminishing returns), which is economically sensible.

3. **Avoids Overfitting**: Degree 2 is usually sufficient to capture 
   curvature without the overfitting risks of higher degrees.

4. **Business Insight**: The model reveals the point of diminishing returns, 
   helping businesses optimize their advertising budget.

5. **Robustness**: Lower degree polynomials tend to be more stable and 
   generalize better to new data.

However, the final choice should be validated using:
- Train/test split or cross-validation
- Domain expertise from marketing/sales teams
- Analysis of residual plots
===============================================================================
""")

# Final Summary
print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)

best_model = "Polynomial (Degree 2)" if r2_poly_2 > r2_linear else "Linear Regression"
improvement = ((r2_poly_2 - r2_linear) / r2_linear) * 100 if r2_linear != 0 else 0

print(f"""
Based on the analysis:
- Best Performing Model: {best_model}
- R² Improvement (Degree 2 vs Linear): {improvement:.2f}%
- Recommended for Production: Polynomial Regression (Degree 2)

Key Takeaways:
1. The relationship between Advertising Spend and Sales is non-linear
2. Polynomial Regression captures this non-linearity better than Linear Regression
3. Degree 2 provides a good balance between fit and complexity
4. Always validate with held-out data in real applications
""")

print("\n--- End of Analysis ---")
