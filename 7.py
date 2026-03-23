students = {
    "Alice": {"marks": [85, 90, 78]},
    "Bob": {"marks": [88, 76, 92]}
}

students["Charlie"] = {"marks": [95, 85, 80]}

students["Alice"]["marks"].append(88)

for name, data in students.items():
    avg = sum(data["marks"]) / len(data["marks"])
    data["average"] = avg

topper = max(students.items(), key=lambda x: x[1]["average"])
print("Students:", students)
print("Topper:", topper[0], "with average", topper[1]["average"])