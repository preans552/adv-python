menu = {
    "Pizza": 200,
    "Burger": 100,
    "Pasta": 150,
    "Coffee": 50
}

order = []
tax_rate = 0.05 

while True:
    print("\n--- Restaurant Menu ---")
    for item, price in menu.items():
        print(f"{item}: Rs.{price}")
    print("Type 'done' to finish ordering.")

    choice = input("Enter item: ")

    if choice.lower() == "done":
        break
    elif choice in menu:
        order.append(choice)
        print(f"{choice} added to order.")
    else:
        print("Item not found.")


subtotal = sum(menu[item] for item in order)
tax = subtotal * tax_rate
total = subtotal + tax

print("\n--- Bill ---")
print("Items ordered:", order)
print("Subtotal:", subtotal)
print("Tax:", tax)
print("Total:", total)