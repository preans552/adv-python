stock = {"keyboard": 5, "apple": 3}
valid_coupons = ["SAVE20"]

def place_order(product, coupon, payment):
    try:
        if product not in stock:
            raise Exception("Product not found")

        if stock[product] == 0:
            raise Exception("Out of stock")

        if coupon and coupon not in valid_coupons:
            raise Exception("Invalid coupon code")

        if payment not in ["UPI", "CARD", "COD", "EMI"]:
            raise Exception("Invalid payment method")

        stock[product] -= 1
        print("Order placed successfully")

    except Exception as e:
        print("Order failed:", e)
