# Two parent class with one child class example 

class Employee:
    def __init__(self, name):
        self.name = name

class AutomationSkills:
    def write_script(self):
        print("Writing Selenium scripts")

class AutomationTester(Employee, AutomationSkills):
    def execute_tests(self):
        print(f"{self.name} is executing automated tests")

# Demonstration
if __name__ == "__main__":
    # Create an AutomationTester object
    tester = AutomationTester("Lakshman Raghu")
    
    # Call methods from both parent classes and its own method
    print(f"Tester Name: {tester.name}")  # From Employee
    tester.write_script()                 # From AutomationSkills
    tester.execute_tests()                # From AutomationTester




