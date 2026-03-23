contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print(f"Added {name}: {number}")

def search_contact(name):
    print(f"{name}: {contacts.get(name, 'Not found')}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name}")
    else:
        print("Contact not found")

def list_contacts():
    for name, number in contacts.items():
        print(name, ":", number)

add_contact("Alice", "12345")
add_contact("Bob", "67890")
search_contact("Alice")
delete_contact("Bob")
list_contacts()