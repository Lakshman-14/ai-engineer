import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'Module': ['AI', 'ML', 'Python', 'DataStructures'],
    'Teamsize': [135, 125, 125, 115]
}
df = pd.DataFrame(data)
print(df)

# Create a pie chart
plt.figure(figsize=(8, 5))
plt.pie(df['Teamsize'], labels=df['Module'], autopct='%1.1f%%', startangle=90)
plt.title('Team Size Distribution by Module')

# Add a legend
plt.legend(df['Module'], title="Modules", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure the pie chart is circular
plt.axis('equal')

# Display the plot
plt.show()