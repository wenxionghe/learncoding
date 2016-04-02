class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        print('This is a ' + self.color + ' ' + self.model + ' with ' +  str(self.mpg) + ' MPG.')
    def drive_car(self):
        self.condition = "used"
        return self.condition
my_car = Car("DeLorean", "silver", 88)

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
    def drive_car(self):
        self.condition = "like new"
        return self.condition
my_car = ElectricCar("Tesla", "silver", 88, "molten salt")

print(my_car.condition)
print(my_car.drive_car())