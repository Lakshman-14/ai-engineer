import pandas as pd

# Read the CSV file
df = pd.read_csv("test_results.csv")
# PATH = /Users/lakshmanraghu/Documents/testPY/test_results.csv

# Univariate Analysis
print("\nUnvariate Analysis of Duration:")
print("-" * 30)
print("\nDescriptive Statistics for Duration:")
print(df["Duration"].describe())

# Bivariate Analysis
print("\nBivariate Analysis (Status vs Duration):")
print("-" * 30)
print("\nAverage Duration by Status:")
status_duration = df.groupby("Status")["Duration"].mean()
print(status_duration)

# Multivariate Analysis
print("\nMultivariate Analysis:")
print("-" * 30)
print("\nDefects by TestCase and Status:")
testcase_status = df.groupby(["TestCase", "Status"])["Duration"].mean()
print(testcase_status)

# Create a pivot table for visualization
pivot_table = df.pivot_table(
    values="Duration",
    index="TestCase",
    columns="Status",
    aggfunc="mean",
    fill_value=0
)
print("\nPivot Table of Duration (TestCase vs Status):")
print(pivot_table)