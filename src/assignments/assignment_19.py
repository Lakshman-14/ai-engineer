import numpy as np

# single-dimensional array
arr = np.array([10, 20, 30, 40, 50, 60])
print("Original array:", arr)
print("Dimensions of original array:", arr.ndim)

# Slice the array using [2:]
slice1 = arr[2:]
print("\nSlicing array[2:]:", slice1)
print("Dimensions of sliced array:", slice1.ndim)

# Slice the array using [3:5]
slice2 = arr[3:5]
print("\nSlicing array[3:5]:", slice2)
print("Dimensions of sliced array:", slice2.ndim)

# Access element using [-4]
element = arr[-4]
print("\nElement at index [-4]:", element)

# Reverse the array
reversed_arr = arr[::-1]
print("\nReversed array:", reversed_arr)
print("Dimensions of reversed array:", reversed_arr.ndim)
