import pandas as pd

# Load the dataset
file_path = "/Users/lakshmanraghu/Downloads/AI Engineer/EDA/SalesDataset.csv"
df = pd.read_csv(file_path)

# 1. 25th percentile of Total Amount
percentile_25 = df['Total Amount'].quantile(0.25)

# 2. 50th percentile of Total Amount
percentile_25 = df['Total Amount'].quantile(0.5)

# 3. 75th percentile of Total Amount
percentile_75 = df['Total Amount'].quantile(0.75)

# 4. Variance in Total Amount
variance_total_amount = df['Total Amount'].var()

# 5. Variance in Quantity sold
variance_quantity = df['Quantity'].var()

# 6. Correlation between Age and Total Amount
correlation_age_total = df['Age'].corr(df['Total Amount'])

# 7. Correlation between Quantity and Total Amount
correlation_quantity_total = df['Quantity'].corr(df['Total Amount'])

# 8. Correlation between Price per Unit and Total Amount
correlation_price_total = df['Price per Unit'].corr(df['Total Amount'])

# Display Results
print(f"\n 25th percentile of Total Amount: {percentile_25}")
print(f"\n 50th percentile of Total Amount: {percentile_25}")
print(f"\n 75th percentile of Total Amount: {percentile_75}")
print(f"\n Variance in Total Amount: {variance_total_amount}")
print(f"\n Variance in Quantity sold: {variance_quantity}")
print(f"\n Correlation between Age and Total Amount: {correlation_age_total}")
print(f"\n Correlation between Quantity and Total Amount: {correlation_quantity_total}")
print(f"\n Correlation between Price per Unit and Total Amount: {correlation_price_total}")