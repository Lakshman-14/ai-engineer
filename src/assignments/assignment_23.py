import pandas as pd

execution_times = pd.Series([12, 15, 20, 18, 25, 30, 22])
print("Execution Times Series:")
print(execution_times)

#Using Slicing (default index)
middle_three = execution_times[2:5]
print("Middle Three (slicing):")
print(middle_three)

#Using .iloc (position-based)
middle_three_iloc = execution_times.iloc[2:5]
print("Middle Three (.iloc):")
print(middle_three_iloc)

# Using .loc (label-based)
middle_three_loc = execution_times.loc[2:4]   # labels 2 through 4 (inclusive)
print("Middle Three (.loc):")
print(middle_three_loc)


