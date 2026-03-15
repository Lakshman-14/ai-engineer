import pandas as pd

# Create a Pandas Series representing test execution times
test_times = pd.Series([12, 15, 20, 18, 25, 30, 22], 
                      index=['TC1', 'TC2', 'TC3', 'TC4', 'TC5', 'TC6', 'TC7'])

# Print the entire Series & Displays the first 3 test times.
print("\nAll test execution times:")
print(test_times)
print("\nFirst 3 test times:")
print(test_times.head(3))

# Calculating and printing the mean execution time of all test cases with 2 decimal places
# Formats the output to 2 decimal places using .2f
print(f"\nMean execution time: {test_times.mean():.2f}")

# Use iloc to print the 2nd test time (index-based)
print(f"\nSecond test time (using iloc): {test_times.iloc[1]}")

# Use loc to print execution time of TC3 (label-based)
print(f"TC3 execution time (using loc): {test_times.loc['TC3']}")
