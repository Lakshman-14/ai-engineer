import pandas as pd

# Step 1: Creation of Dictionary
test_cases = {
    "Alex": 500,
    "Steve": 200,
    "Bob": 300
}

# Step 2: Convert Dictionary → Pandas Series
test_series = pd.Series(test_cases)
print("\nTest Cases Executed by Engineers:")
print(test_series)


# Get test cases executed by Alex
print("\nAlex executed:", test_series["Alex"])

# Slice for Steve & Bob
print("\nSteve & Bob test cases:")
print(test_series[["Steve", "Bob"]])
