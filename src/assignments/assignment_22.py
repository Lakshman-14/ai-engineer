import pandas as pd

# Create a Pandas Series (scalar values inside)
execution_times = pd.Series([12, 15, 20, 18, 25, 30, 22])

print("Execution Times Series:")
print(execution_times)

# --------------------------------------------------------------------------

# Slice the Middle Three Execution Times
middle_three = execution_times[2:5]   # slicing (index 2 to 4)
print("Middle Three Execution Times:")
print(middle_three)
