class Vehicle:
    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.fuel = 4  # full tank

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

    # open the window
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
my_mc.drive()  # out of fuel
my_car.drive()

my_car.radio()
my_car.window()
my_mc.helmet()
# my_mc.window() # windows do not exist on motorcycles
