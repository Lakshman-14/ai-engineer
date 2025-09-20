# Step 1: Create a list of 5 employee names
employees = ["BradPit", "Lakshman", "Virat", "Babu", "Sai"]

# Step 2: Use a for loop with enumerate to print numbered names
for i, n in enumerate(employees, start=1):
    print(f"{i}. {n}")
