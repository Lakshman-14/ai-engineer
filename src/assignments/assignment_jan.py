import csv

class TestCase:
    """
    Represents a manual test case.
    """
    def __init__(self, test_id, test_name, module, status="Not Executed"):
        self.test_id = test_id
        self.test_name = test_name
        self.module = module
        self.status = status

    def execute_test(self, result):
        """
        Updates the test status based on the result provided (Pass or Fail).
        """
        # Normalize input to manage case insensitivity
        res_lower = result.strip().lower()
        if res_lower in ['pass', 'p']:
            self.status = "Pass"
        elif res_lower in ['fail', 'f']:
            self.status = "Fail"
        else:
            # If input is neither Pass nor Fail (or variations), keep original status or mark invalid
            # Requirement says "Pass/Fail". We'll just ignore invalid but usually one might set "Skip" or keep "Not Executed".
            pass

    def display_test_case(self):
        """
        Prints test case details.
        """
        print(f"ID: {self.test_id} | Name: {self.test_name} | Module: {self.module} | Status: {self.status}")

    def to_csv_row(self):
        """
        Returns test details in list format for CSV writing.
        Last column is Automation Tool, which is 'NA' for manual tests.
        """
        return [self.test_id, self.test_name, self.module, self.status, "NA"]


class AutomatedTestCase(TestCase):
    """
    Represents an automated test case, inheriting from TestCase.
    """
    def __init__(self, test_id, test_name, module, automation_tool, status="Not Executed"):
        # Use super() to initialize parent attributes
        super().__init__(test_id, test_name, module, status)
        self.automation_tool = automation_tool

    def display_test_case(self):
        """
        Overrides display_test_case to show automation tool.
        """
        print(f"ID: {self.test_id} | Name: {self.test_name} | Module: {self.module} | Status: {self.status} | Tool: {self.automation_tool}")

    def to_csv_row(self):
        """
        Overrides to_csv_row to include the actual automation tool name.
        """
        return [self.test_id, self.test_name, self.module, self.status, self.automation_tool]


class TestSuite:
    """
    Manages multiple test cases.
    """
    def __init__(self, suite_name):
        self.suite_name = suite_name
        self.tests = []

    def add_test(self, test_case):
        """
        Adds a test case object to the suite.
        """
        self.tests.append(test_case)

    def run_all_tests(self):
        """
        Executes all tests by asking the user to enter Pass/Fail for each.
        """
        print(f"\n--- Running Test Suite: {self.suite_name} ---")
        for test in self.tests:
            test.display_test_case()
            result = input(f"Enter result for 'Test ID {test.test_id}' (Pass/Fail): ")
            test.execute_test(result)
            print("-" * 30)

    def save_results_to_csv(self, file_name):
        """
        Saves all test execution results into a CSV file.
        """
        header = ["Test ID", "Test Name", "Module", "Status", "Automation Tool"]
        
        try:
            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                for test in self.tests:
                    writer.writerow(test.to_csv_row())
            print(f"\nResults successfully saved to '{file_name}'")
        except IOError as e:
            print(f"Error saving to CSV file: {e}")

    def summary_report(self):
        """
        Displays a summary of the test execution.
        """
        total = len(self.tests)
        passed = sum(1 for t in self.tests if t.status == "Pass")
        failed = sum(1 for t in self.tests if t.status == "Fail")
        not_executed = total - (passed + failed)

        print("\n--- Execution Summary Report ---")
        print(f"Total Tests    : {total}")
        print(f"Passed Tests   : {passed}")
        print(f"Failed Tests   : {failed}")
        print(f"Not Executed   : {not_executed}")
        print("--------------------------------")


if __name__ == "__main__":
    # --- Main Program Execution ---

    # 1. Create a TestSuite
    my_suite = TestSuite("Regression Cycle Jan")

    # 2. Create 2 Manual Test Cases
    tc1 = TestCase(101, "Verify Login", "Auth")
    tc2 = TestCase(102, "Verify Profile Update", "User Profile")

    # 3. Create 2 Automated Test Cases
    atc1 = AutomatedTestCase(201, "Search Product", "Search", "Selenium")
    atc2 = AutomatedTestCase(202, "Add to Cart", "Checkout", "Playwright")

    # 4. Add all test cases to the test suite
    my_suite.add_test(tc1)
    my_suite.add_test(tc2)
    my_suite.add_test(atc1)
    my_suite.add_test(atc2)

    # 5. Execute the tests
    # Note: When running this, you will be prompted to enter Pass/Fail for each test.
    my_suite.run_all_tests()

    # 6. Save results to CSV
    csv_filename = "test_results.csv"
    my_suite.save_results_to_csv(csv_filename)

    # 7. Print the execution summary
    my_suite.summary_report()
