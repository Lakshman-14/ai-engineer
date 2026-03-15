import pandas as pd

# Step 1: Create test data as a dictionary
data = {
    'TestCase': ['TC1', 'TC2', 'TC3', 'TC4', 'TC5'],
    'Status': ['Passed', 'Failed', 'Passed', 'Failed', 'Passed'],
    'Duration': [12, 15, 20, 18, 25]
}

# Create DataFrame from the dictionary
df = pd.DataFrame(data)

# Step 2: Print the original DataFrame
print("Original DataFrame:")
print("=" * 50)
print(df)
print("\n")

# Step 3: Select and print only the Status column
print("Status Column:")
print("=" * 50)
print(df['Status'])
print("\n")

# Step 4: Filter and print only Failed test cases
print("Failed Test Cases:")
print("=" * 50)
failed_tests = df[df['Status'] == 'Failed']
print(failed_tests)
print("\n")

# Step 5: Save DataFrame to CSV
csv_file = "test_results.csv"
df.to_csv(csv_file, index=False)
print(f"DataFrame saved to {csv_file}")
print("\n")

# Step 6: Read back the CSV into a new DataFrame
print("DataFrame read from CSV:")
print("=" * 50)
new_df = pd.read_csv(csv_file)
# Handle any potential missing values by filling with mean duration
new_df['Duration'] = new_df['Duration'].fillna(new_df['Duration'].mean())
print(new_df)
