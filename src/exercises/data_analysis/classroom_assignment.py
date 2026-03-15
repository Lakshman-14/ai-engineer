import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set style for better visualization
plt.style.use('classic')

# Question 1: Create and print two DataFrames
print("Question 1:")
df1 = pd.DataFrame({
    'Values': [10, 20, 30]
})
df2 = pd.DataFrame({
    'Values': [30, 40, 50]
})
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Plotting Question 1
plt.figure(figsize=(10, 5))
x = range(len(df1))
plt.bar(x, df1['Values'], width=0.4, align='edge', label='DataFrame 1', alpha=0.7)
plt.bar(x, df2['Values'], width=-0.4, align='edge', label='DataFrame 2', alpha=0.7)
plt.title('Comparison of DataFrame 1 and DataFrame 2')
plt.xlabel('Index')
plt.ylabel('Values')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('question1_plot.png')
plt.close()
print("\nPlot saved as 'question1_plot.png'")
print()

# Question 2: Add the DataFrames and print result
print("Question 2:")
result_df = df1 + df2
print("Sum of DataFrames:")
print(result_df)

# Plotting Question 2
plt.figure(figsize=(8, 5))
plt.plot(result_df['Values'], marker='o', linewidth=2, markersize=10)
plt.title('Sum of DataFrames')
plt.xlabel('Index')
plt.ylabel('Sum Values')
plt.grid(True, alpha=0.3)
plt.savefig('question2_plot.png')
plt.close()
print("\nPlot saved as 'question2_plot.png'")
print()

# Question 3: Create and print two DataFrames
print("Question 3:")
df3 = pd.DataFrame({
    'Values': [100, 200, 300]
})
df4 = pd.DataFrame({
    'Values': [400, 500]
})
print("DataFrame 3:")
print(df3)
print("\nDataFrame 4:")
print(df4)

# Plotting Question 3
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
df3['Values'].plot(kind='bar')
plt.title('DataFrame 3')
plt.ylabel('Values')
plt.subplot(1, 2, 2)
df4['Values'].plot(kind='bar')
plt.title('DataFrame 4')
plt.tight_layout()
plt.savefig('question3_plot.png')
plt.close()
print("\nPlot saved as 'question3_plot.png'")
print()

# Question 4: Append df4 to df3
print("Question 4:")
combined_df = pd.concat([df3, df4], ignore_index=True)
print("Combined DataFrame:")
print(combined_df)

# Plotting Question 4
plt.figure(figsize=(10, 5))
combined_df['Values'].plot(kind='bar')
plt.title('Combined DataFrame Values')
plt.xlabel('Index')
plt.ylabel('Values')
plt.grid(True, alpha=0.3)
plt.savefig('question4_plot.png')
plt.close()
print("\nPlot saved as 'question4_plot.png'")
print()

# Question 5: Create and print DataFrame with multiple columns
print("Question 5:")
data_dict = {
    'Mani': [10, 20, 30],
    'Alex': [20, 30, None]  # Added None to match the length
}
result_df = pd.DataFrame(data_dict)
print("DataFrame from dictionary:")
print(result_df)

# Plotting Question 5
plt.figure(figsize=(10, 5))
result_df.plot(kind='bar', width=0.8)
plt.title('Comparison of Mani and Alex Values')
plt.xlabel('Index')
plt.ylabel('Values')
plt.legend(title='Person')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('question5_plot.png')
plt.close()
print("\nPlot saved as 'question5_plot.png'")
