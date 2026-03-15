import pandas as pd

# Step 1: Create test data as a dictionary
data = {
    'TestCase': ['TC1', 'TC2', 'TC3', 'TC4', 'TC5', 'TC6'],
    'Module': ['Login', 'Login', 'Payment', 'Payment', 'Reports', 'Reports'],
    'Status': ['Passed', 'Failed', 'Passed', 'Failed', 'Passed', 'Passed'],
    'Duration': [12, 15, 20, 18, 25, 22]
}

# Create DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print("=" * 50)
print(df)
print("\n")

# Step 2: Group by Status and count "PASSED vs FAILED"
print("Test Cases Status Distribution (PASSED vs FAILED):")
print("=" * 50)
status_summary = df.groupby("Status")["TestCase"].count()
print(f"PASSED Tests: {status_summary.get('Passed', 0)}")
print(f"FAILED Tests: {status_summary.get('Failed', 0)}")
print(f"Pass Rate: {(status_summary.get('Passed', 0) / len(df) * 100):.1f}%")
print("\n")

# Step 3: Group by Module and Find average duration per module
print("Average Test Duration per Module:")
print("=" * 50)
module_summary = df.groupby("Module")["Duration"].mean()
for module, duration in module_summary.items():
    print(f"{module} Module: {duration:.1f} seconds")
print("\n")

# Additional Analysis: Show full summary with multiple metrics
print("Detailed Module Summary (Multiple Metrics):")
print("=" * 50)
detailed_summary = df.groupby("Module").agg({
    'Duration': ['mean', 'min', 'max'],
    'TestCase': 'count'
})
print(detailed_summary)
