def calculate_salary(basic, hra, da, bonus=0):
    
    return basic + hra + da + bonus

# Example usage without bonus
employeesalary1 = calculate_salary(30000, 8000, 5000)
print("\nSalary (without bonus):", employeesalary1)

# Example usage with bonus
employeesalary2 = calculate_salary(30000, 8000, 5000, 4000)
print("\nSalary (with bonus):", employeesalary2)
