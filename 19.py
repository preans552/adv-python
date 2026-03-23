class Vehicle:
    total_rented = 0  

    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def calculate_rent(self, days):
        Vehicle.total_rented += 1
        return self.rate * days

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name, rate=1000)

class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name, rate=300)

class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name, rate=2000)


c = Car("Sedan")
b = Bike("Yamaha")
t = Truck("Volvo")

print("Car rent:", c.calculate_rent(3))
print("Bike rent:", b.calculate_rent(5))
print("Truck rent:", t.calculate_rent(2))
print("Total vehicles rented:", Vehicle.total_rented)