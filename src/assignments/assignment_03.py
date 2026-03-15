def calculate_bill(item_cost, quantity, tax=0.05, discount=0):
  
    total = (item_cost * quantity) + (item_cost * quantity * tax) - discount
    return total

# Test Case 1: Only positional arguments (using default tax and discount)
print("Bill 1:", calculate_bill(500, 2))

# Test Case 2: With custom tax rate
print("Bill 2:", calculate_bill(500, 2, tax=0.1))

# Test Case 3: With custom discount
print("Bill 3:", calculate_bill(500, 2, discount=50))

# Test Case 4: With both custom tax and discount
print("Bill 4:", calculate_bill(500, 2, tax=0.08, discount=100))
