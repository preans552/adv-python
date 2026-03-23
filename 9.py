employees = {}

while True:
    print("\n--- Employee Attendance Menu ---")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Display Employees")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        employees[name] = "Present"
        print(f"{name} added.")
    elif choice == "2":
        name = input("Enter employee name to remove: ")
        if name in employees:
            del employees[name]
            print(f"{name} removed.")
        else:
            print("Employee not found.")
    elif choice == "3":
        if employees:
            print("Employees:", list(employees.keys()))
        else:
            print("No employees recorded.")
    elif choice == "4":
        print("Exiting system...")
        break
    else:
        print("Invalid choice. Try again.")