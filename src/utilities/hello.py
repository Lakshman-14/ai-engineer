print("Welcome to TEST LEAF")

# Get user input for age and experience
age = input("Please enter your age: ")
experience = input("Please enter your years of IT experience: ")

# Convert input to integers
age = int(age)
experience = int(experience)

# Check conditions and print appropriate message
if age >= 22 and experience >= 2:
    print("Access Granted")
else:
    print("Access Denied")

print("BYE")