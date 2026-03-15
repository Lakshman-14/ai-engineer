from shopping_utils import calculate_bill

# Test Case 1: Only positional arguments (using default tax and discount)
bill1 = calculate_bill(500, 2)
print("Bill 1:", bill1)

# Test Case 2: With custom tax rate
bill2 = calculate_bill(500, 2, tax=0.1)
print("Bill 2:", bill2)

# Test Case 3: With custom discount
bill3 = calculate_bill(500, 2, discount=50)
print("Bill 3:", bill3)

# Test Case 4: With both custom tax and discount
bill4 = calculate_bill(500, 2, tax=0.08, discount=100)
print("Bill 4:", bill4)

# Additional demonstration of flexibility
print("\nAdditional Examples:")
# Higher quantity, default tax and discount
print("Large order:", calculate_bill(100, 10))
# Custom tax rate only (15%)
print("Special tax region:", calculate_bill(200, 3, tax=0.15))
# High value order with special discount
print("Special discount:", calculate_bill(1000, 2, discount=250))
