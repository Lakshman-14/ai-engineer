import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
file_path = "test_results_missing.csv"
df = pd.read_csv(file_path)

# Count missing values in each column
print("Missing values per column:")
print(df.isnull().sum())

# Replace missing Duration with the mean duration
mean_duration = df['Duration'].mean()
df['Duration'].fillna(mean_duration, inplace=True)

# Replace missing Status with "Unknown"
df['Status'].fillna("Unknown", inplace=True)

# Drop any row that still contains missing values
df.dropna(inplace=True)

# Print the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)
