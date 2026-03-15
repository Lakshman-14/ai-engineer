import pandas as pd
import matplotlib.pyplot as plt

# Create a figure with subplots
# Create the data dictionary
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Week1": [1000, 2000, 3000, 5000, 7000, 8000, 6700],
    "Week2": [4000, 5000, 2500, 4500, 3500, 5000, 5600],
    "Week3": [5000, 6000, 4500, 3500, 2000, 6000, 4800],
    "Week4": [6000, 5000, 2900, 4500, 3500, 4500, 4500]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set 'Day' as the index
df.set_index('Day', inplace=True)

# Create a figure with subplots
plt.figure(figsize=(20, 12))

# 1. Line Plot
plt.subplot(2, 2, 1)
df.plot(kind='line', marker='o')
plt.title('Weekly Data - Line Plot')
plt.xlabel('Days')
plt.ylabel('Values')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.02, 0.5), loc='center left')

# 2. Bar Plot
plt.subplot(2, 2, 2)
df.plot(kind='bar', width=0.8)
plt.title('Weekly Data - Bar Plot')
plt.xlabel('Days')
plt.ylabel('Values')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.02, 0.5), loc='center left')

# 3. Histogram
plt.subplot(2, 2, 3)
df.plot(kind='hist', bins=10, alpha=0.5)
plt.title('Distribution of Values - Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.02, 0.5), loc='center left')

# 4. Pie Chart
plt.subplot(2, 2, 4)
daily_totals = df.sum(axis=1)  # Calculate total for each day
plt.pie(daily_totals.values, 
        labels=daily_totals.index,
        autopct='',  # Empty string to remove percentage labels
        startangle=90)
plt.title('Total Values Distribution by Day')
plt.axis('equal')  # Ensure the pie chart is circular

# Adjust layout to prevent overlap
plt.subplots_adjust(wspace=0.3, hspace=0.3, right=0.85)

# Show all plots
plt.show()

# Optional: Reading from CSV file
# Uncomment the following lines if you want to read from a CSV file
'''
try:
    df_from_csv = pd.read_csv("/Users/lakshmanraghu/Downloads/data1.csv")
    
    # Create plots using df_from_csv
    plt.figure(figsize=(15, 10))
    
    # Line plot
    plt.subplot(2, 2, 1)
    df_from_csv.plot(kind='line', marker='o')
    plt.title('CSV Data - Line Plot')
    
    # Bar plot
    plt.subplot(2, 2, 2)
    df_from_csv.plot(kind='bar')
    plt.title('CSV Data - Bar Plot')
    
    # Histogram
    plt.subplot(2, 2, 3)
    df_from_csv.plot(kind='hist', bins=10, alpha=0.5)
    plt.title('CSV Data - Histogram')
    
    plt.tight_layout()
    plt.show()
except FileNotFoundError:
    print("CSV file not found. Using default data instead.")
except Exception as e:
    print(f"Error reading CSV file: {e}")
'''