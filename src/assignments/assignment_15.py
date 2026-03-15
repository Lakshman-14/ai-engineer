class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size
    
    def show_details(self):
        print(f"Manager Details:")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Team Size: {self.team_size}")

# Demonstration
def main():
    # Create a Manager object
    manager = Manager("Lakshman Raghu", "EMP014", 5)
    
    # Display all attributes using show_details method
    manager.show_details()

if __name__ == "__main__":
    main()
