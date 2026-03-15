import numpy as np

# Create a three-dimensional array
sample3dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Original three-dimensional array:")
print(sample3dim)
print("\nDimensions of array:", sample3dim.ndim)

# Access element at [0][0][0]
try:
    print("\nElement at sample3dim[0][0][0]:", sample3dim[0][0][0])
except IndexError as e:
    print("Error accessing sample3dim[0][0][0]:", e)

# Access element at [0][1][2]
try:
    print("Element at sample3dim[0][1][2]:", sample3dim[0][1][2])
except IndexError as e:
    print("Error accessing sample3dim[0][1][2]:", e)

# Access element at [1][1][2]
try:
    print("Element at sample3dim[1][1][2]:", sample3dim[1][1][2])
except IndexError as e:
    print("Error accessing sample3dim[1][1][2]:", e)


