class OutOfStockError(Exception):
    pass

class InvalidProductIDError(Exception):
    pass


inventory = {"PRODUCT1": 10, "PRODUCT102": 0}

def purchase(product_id):
    try:
        if product_id not in inventory:
            raise InvalidProductIDError("Invalid Product ID")

        if inventory[product_id] == 0:
            raise OutOfStockError("Product is out of stock")

        inventory[product_id] -= 1
        print("PRODUCT PURCHASED SUCCESSFUL")

    except (OutOfStockError, InvalidProductIDError) as e:
        print("Error:", e)
