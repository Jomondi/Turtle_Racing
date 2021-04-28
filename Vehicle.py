class Vehicle:
    def __init__(self, name, max_speed, mileage, price):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.price = price

    def description(self):
        desc = "%s has a maximum speed of %s mph, it also has %s miles and retails for %s dollars." % \
               (self.name, self.max_speed, self.mileage, self.price)
        return desc


# modelX = Vehicle(240, 18)
# print(modelX.max_speed, modelX.mileage)
car1 = Vehicle('Toyota', 200, 100, 24000)
car2 = Vehicle('Tesla', 240, 0, 38000)
print(car1.description())
print(car2.description())
