import pandas as pd

# Create Series for test pass percentage
pass_rates = pd.Series([80, 85, 78, 90, 88], index=['B1', 'B2', 'B3', 'B4', 'B5'])

# Print the Series
print("\nTest Pass Rates:")
print(pass_rates)

# Calculate and print Average pass rate
average_rate = pass_rates.mean()
print(f"\nAverage PASS Rate: {average_rate:.2f}%")

# Find build with highest pass rate
highest_build = pass_rates.idxmax()
highest_rate = pass_rates.max()
print(f"\nBuild {highest_build} had the highest pass rate: {highest_rate}%")

# Using iloc to get the last build's pass rate
last_build_rate = pass_rates.iloc[-1]
print(f"\nLast build pass rate (using iloc): {last_build_rate}%")

# Using loc to get B3's pass rate
b3_rate = pass_rates.loc['B3']
print(f"\nBuild B3 pass rate (using loc): {b3_rate}%")

# Normalize values by subtracting the mean
normalized_rates = pass_rates - average_rate
print("\nNormalized pass rates (difference from mean):")
print(normalized_rates)
