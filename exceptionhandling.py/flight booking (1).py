seats = 2

def book_ticket(name, payment):
    global seats
    try:
        if name == "":
            raise ValueError("Invalid passenger name")

        if seats == 0:
            raise Exception("No seats available")

        if payment not in ["CARD", "UPI"]:
            raise Exception("Payment failed")

        seats -= 1
        print("Ticket booked for", name)

    except Exception as e:
        print("Booking failed:", e)
