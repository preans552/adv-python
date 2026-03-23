student_marks = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("Initial:", student_marks)

student_marks["David"] = 88
print("After adding:", student_marks)

student_marks["Alice"] = 92
print("After updating:", student_marks)

del student_marks["Charlie"]
print("After deleting:", student_marks)

print("Keys:", student_marks.keys())
print("Values:", student_marks.values())
print("Items:", student_marks.items())