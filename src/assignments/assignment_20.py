import numpy as np

# Create a two-dimensional array
sample_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Original two-dimensional array:")
print(sample_array)
print("Dimensions of array:", sample_array.ndim)

# Access element at [0][1]
try:
    print("\nElement at sample_array[0][1]:", sample_array[0][1])
except IndexError as e:
    print("Error accessing sample_array[0][1]:", e)

# Access element at [1][1]
try:
    print("Element at sample_array[1][1]:", sample_array[1][1])
except IndexError as e:
    print("Error accessing sample_array[1][1]:", e)

# Access element at [0][3]
try:
    print("Element at sample_array[0][3]:", sample_array[0][3])
except IndexError as e:
    print("Error accessing sample_array[0][3]:", e)

# Calculate sum of all elements
array_sum = np.sum(sample_array)
print("\nSum of all elements in the array:", array_sum)
