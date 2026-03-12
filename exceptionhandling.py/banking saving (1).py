accounts = {
    "A101": 5000,
    "A102": 3000
}

def transfer(from_acc, to_acc, amount):
    try:
        if from_acc not in accounts or to_acc not in accounts:
            raise Exception("Invalid account number")

        if accounts[from_acc] < amount:
            raise Exception("Insufficient balance")

        accounts[from_acc] -= amount
        accounts[to_acc] += amount

        print("Transaction successful")

    except Exception as e:
        print("Transaction failed:", e)
