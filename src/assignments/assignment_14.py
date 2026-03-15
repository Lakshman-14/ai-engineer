class Employee:
    """
    Base class representing an Employee
    
    Attributes:
        name (str): Name of the employee
        employee_id (str): Unique identifier for the employee
    """

    
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def display_info(self):
        """Display basic employee information"""
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")


class Tester(Employee):
    """
    Child class representing a Tester, inheriting from Employee
    Additional functionality for running tests
    """
    
    def __init__(self, name, employee_id, test_tools=None):
        # Call parent class constructor
        super().__init__(name, employee_id)
        # Additional attribute specific to Tester
        self.test_tools = test_tools or ["Selenium", "PyTest"]
    
    def run_tests(self):
        """Method to simulate running automation tests"""
        print(f"{self.name} is running automation tests")
    
    def display_info(self):
        """Override parent's display_info to include test tools"""
        super().display_info()
        print(f"Role: Tester")
        print(f"Testing Tools: {', '.join(self.test_tools)}")


# Demonstrate the inheritance
if __name__ == "__main__":
    # Create a Tester object
    tester1 = Tester("John Smith", "T001", ["Selenium", "PyTest", "Robot Framework"])
    
    print("=== Tester Information ===")
    tester1.display_info()  # This will call the overridden method
    
    print("\n=== Running Tests ===")
    tester1.run_tests()  # This will call the child-specific method
    
    # Create another tester using default test tools
    tester2 = Tester("Alice Johnson", "T002")
    print("\n=== Second Tester Information ===")
    tester2.display_info()
