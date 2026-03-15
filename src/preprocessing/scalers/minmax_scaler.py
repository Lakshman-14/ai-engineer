from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Sample data
data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
print("\nOriginal Data:")
print(data)

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

print("\nTransformed Data (Min-Max Scaled):")
print(scaled_data)

# Data min and max learned by the scaler
print("\nMin of each column:", scaler.data_min_)
print("Max of each column:", scaler.data_max_)

# 25th and 75th percentiles
percentile_25 = np.percentile(data, 25, axis=0)
percentile_75 = np.percentile(data, 75, axis=0)
print("25th Percentile of each column:", percentile_25)
print("75th Percentile of each column:", percentile_75)
