#Step 1 :  Create a NumPy Array
import numpy as np 
# Defects count as NumPy array
defects_array = np.array([10, 20, 23, 45, 50])
print("\nNumPy Array of Defects:")
print(defects_array)


# Step 2 : Convert NumPy Array → Pandas Series 
import pandas as pd
# Convert NumPy array to Pandas Series
defects_series = pd.Series(defects_array, index=["Module1", "Module2", "Module3", "Module4", "Module5"])
print("\nPandas Series of Defects:")
print(defects_series)


# Get defects in Module3
print("\nDefects in Module3:", defects_series["Module3"])

# Get defects from Module2 to Module4
print(defects_series["Module2":"Module4"])