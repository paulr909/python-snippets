class Vehicle:  # Base Vehicle class
    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.gas = 4  # a full tank of gas

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print(f"The {self.color} {self.manufacturer} goes VROOOM!")
        else:
            print(f"The {self.color} {self.manufacturer} sputters out of gas.")


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
        print(f"The {self.color} {self.manufacturer} goes whoosh!")


# create and use an electric car
my_ecar = ECar("white", "Nissan")
my_ecar.window()
my_ecar.radio()
my_ecar.color()
my_ecar.drive()
my_ecar.drive()
my_ecar.drive()

# access the lingering gas tank
print(my_ecar.gas)
