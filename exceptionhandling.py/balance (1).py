balance = 5000

try:
    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        raise Exception("Overdraft! Not enough balance")

    balance -= amount
    print("Transaction successful")
    print("Remaining balance:", balance)

except ValueError:
    print("Invalid amount")

except Exception as e:
    print("Error:", e)
