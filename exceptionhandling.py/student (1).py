students = {}

try:
    sid = int(input("Enter Student ID: "))
    grade = input("Enter Grade (A/B/C/D/F): ").upper()

    if grade not in ['A', 'B', 'C', 'D', 'F']:
        raise ValueError("Grade must be A, B, C, D, or F")

    students[sid] = grade
    print("Student record saved")
    print(students)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Error:", e)
