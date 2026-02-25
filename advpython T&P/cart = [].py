cart = []

def add_item(name, price, quantity):
    cart.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

def view_cart():
    if not cart:
        print("\nYour cart is empty.")
    else:
        total = 0
        print("\nShopping Cart:")
        for i, item in enumerate(cart):
            cost = item["price"] * item["quantity"]
            total += cost
            print(f"{i+1}. {item['name']} x {item['quantity']} = ₹{cost}")
        print(f"\nTotal: ₹{total}")

def delete_item():
    view_cart()
    if cart:
        try:
            item_no = int(input("Enter item number to delete: "))
            if 1 <= item_no <= len(cart):
                removed = cart.pop(item_no - 1)
                print(f"{removed['name']} removed successfully!")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Invalid input.")

def main():
    while True:
        print("\nSHOPPING CART MENU")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Delete Item")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter item name: ")
            try:
                price = int(input("Enter item price: "))
                quantity = int(input("Enter quantity: "))
                add_item(name, price, quantity)
                print("Item added successfully!")
            except ValueError:
                print("Invalid input.")

        elif choice == "2":
            view_cart()

        elif choice == "3":
            delete_item()

        elif choice == "4":
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
