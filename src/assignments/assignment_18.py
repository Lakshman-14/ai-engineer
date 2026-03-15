def write_initial_results():
    # Create and write initial test results
    with open("report.txt", "w") as file:
        file.write("TestCase1 - Passed\n")
        file.write("TestCase2 - Failed\n")
        file.write("TestCase3 - Passed\n")

def append_more_results():
    # Append additional test results
    with open("report.txt", "a") as file:
        file.write("TestCase4 - Passed\n")
        file.write("TestCase5 - Failed\n")

def generate_summary():
    passed_count = 0
    failed_count = 0
    
    # Read and process the test results
    with open("report.txt", "r") as file:
        for line in file:
            line = line.strip()  # Remove extra newline characters
            if "Passed" in line:
                passed_count += 1
            elif "Failed" in line:
                failed_count += 1
    
    # Calculate total tests
    total_tests = passed_count + failed_count
    
    # Print the summary
    print("Total Tests:", total_tests)
    print("Passed:", passed_count)
    print("Failed:", failed_count)

def main():
    write_initial_results()
    append_more_results()
    generate_summary()

if __name__ == "__main__":
    main()
