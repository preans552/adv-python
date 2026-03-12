contacts = {}

try:
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    if name == "" or phone == "":
        raise ValueError("Fields cannot be empty")

    if name in contacts:
        raise Exception("Duplicate entry")

    contacts[name] = phone
    print("Contact saved")

except Exception as e:
    print("Error:", e)
