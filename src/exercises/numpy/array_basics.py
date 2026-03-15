import numpy as np

# Creating a 1D NumPy array with test execution times
test_times = np.array([10, 15, 20, 25, 30, 35, 40, 45])
print("\n1. Original array:")
print(test_times)

# Indexing
print("\n2. Indexing:")
print(f"First element: {test_times[0]}")
print(f"Last element: {test_times[-1]}")
print(f"Third element: {test_times[2]}")

# Array shape
print("\n3. Array shape:")
print(f"Shape of the array: {test_times.shape}")

# Slicing
print("\n4. Slicing:")
print("First three test times:")
print(test_times[0:3])
print("\nAlternate test times:")
print(test_times[::2])

# Reshaping
print("\n5. Reshaping:")
reshaped_array = test_times.reshape(2, 4)
print("Array reshaped to 2x4:")
print(reshaped_array)

# Joining arrays
more_times = np.array([50, 55, 60, 65])
print("\n6. Joining arrays:")
print("Additional test times:")
print(more_times)
combined_array = np.concatenate([test_times, more_times])
print("\nCombined array:")
print(combined_array)

# Splitting array
print("\n7. Splitting array:")
split_arrays = np.array_split(combined_array, 3)
for i, arr in enumerate(split_arrays, 1):
    print(f"\nSplit {i}:")
    print(arr)
