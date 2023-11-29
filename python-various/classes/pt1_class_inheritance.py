class Vehicle:
    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.fuel = 4  # Full tank

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 1
            print(f"The {self.color} {self.manufacturer} goes VROOOM!")
        else:
            print(f"The {self.color} {self.manufacturer} sputters out of fuel")


class Car(Vehicle):
    @staticmethod
    def radio():
        print("Pumping' Tunes!")

    # Open the window
    @staticmethod
    def window():
        print("Ah... fresh air!")


class Motorcycle(Vehicle):
    @staticmethod
    def helmet():
        print("Nice and safe!")


my_car = Car("red", "Mercedes")
my_mc = Motorcycle("silver", "Suzuki")

my_car.drive()
my_mc.drive()
my_mc.drive()
my_mc.drive()
my_mc.drive()
my_mc.drive()  # Out of fuel
my_car.drive()

my_car.radio()
my_car.window()
my_mc.helmet()
# my_mc.window()  # Windows do not exist on motorcycles
