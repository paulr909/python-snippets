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


class ECar(Car):  # Inherits from Car class
    # an eco-friendly drive method
    def drive(self):
        print(f"The {self.color} {self.manuf} goes whoosh!")


# create and use an electric car
my_ecar = ECar("white", "Nissan")
my_ecar.window()
my_ecar.radio()
my_ecar.drive()

# access the lingering gas tank
print(my_ecar.gas)
