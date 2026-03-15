from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
print("\nOriginal Data:")
print(data)

# Initialize StandardScaler
scaler = StandardScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

print("\nTransformed Data (Standardized):")
print(scaled_data)

# Mean and standard deviation learned by the scaler
print("\nMean of each column:", scaler.mean_)
print("Variance of each column:", scaler.var_)
