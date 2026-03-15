from sklearn.preprocessing import RobustScaler
import numpy as np

# Sample data
data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
print("\nOriginal Data:")
print(data)

# Initialize RobustScaler
scaler = RobustScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

print("\nTransformed Data (Robust Scaled):")
print(scaled_data)

# Median and IQR learned by the scaler
print("\nMedian of each column:", scaler.center_)
print("IQR of each column:", scaler.scale_)

# 25th and 75th percentiles
percentile_25 = np.percentile(data, 25, axis=0)
percentile_75 = np.percentile(data, 75, axis=0)
print("25th Percentile of each column:", percentile_25)
print("75th Percentile of each column:", percentile_75)
