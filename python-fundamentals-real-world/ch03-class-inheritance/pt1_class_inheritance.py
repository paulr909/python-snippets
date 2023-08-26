class Vehicle:  # Base Vehicle class
    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4  # a full tank of gas

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print(f"The {self.color} {self.manuf} goes VROOOM!")
        else:
            print(f"The {self.color} {self.manuf} sputters out of gas.")


class Car(Vehicle):  # Inherits from Vehicle class
    # turn the radio on
    @staticmethod
    def radio():
        print("Pumping' Tunes!")

    # open the window
    @staticmethod
    def window():
        print("Ah... fresh air!")


class Motorcycle(Vehicle):  # Inherits from Vehicle class
    # put on motorcycle helmet
    @staticmethod
    def helmet():
        print("Nice and safe!")


# create car & motorcycle objects
my_car = Car("red", "Mercedes")
my_mc = Motorcycle("silver", "Harley")

# take them out for a test drive
my_car.drive()
my_mc.drive()
my_mc.drive()
my_mc.drive()
my_mc.drive()
my_mc.drive()  # out of gas
my_car.drive()

# play around with accessories
my_car.radio()
my_car.window()
my_mc.helmet()
# my_mc.window() # windows do not exist on motorcycles
