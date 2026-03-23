students = []

while True:
    print("\n--- Student Record Menu ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Filter Pass/Fail")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        marks = int(input("Enter marks: "))
        students.append({"name": name, "roll": roll, "marks": marks})
        print("Student added.")
    elif choice == "2":
        for s in students:
            print(s)
    elif choice == "3":
        for s in students:
            status = "Pass" if s["marks"] >= 40 else "Fail"
            print(f"{s['name']} ({s['roll']}): {status}")
    elif choice == "4":
        print("Exiting system...")
        break
    else:
        print("Invalid choice.")