import pandas as pd

# Create a Pandas Series for defects logged across 7 days
defects = pd.Series([5, 8, 3, 6, 10, 2, 7], 
                    index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

# Print the Series
print("\nDefects logged across the week:")
print(defects)

# Print maximum defects logged in a single day
print("\nMaximum defects in a day:", defects.max())

# Print the day with minimum defects
print("\nDay with minimum defects:", defects.idxmin())

# Use iloc to print defect count of Day5 (Friday)
print("\nDefects on Day5 (using iloc):", defects.iloc[4])

# Use loc to print defect count on Wednesday
print("\nDefects on Wednesday (using loc):", defects.loc['Wed'])

# Print total defects logged in the week
print("\nTotal defects in the week:", defects.sum())
