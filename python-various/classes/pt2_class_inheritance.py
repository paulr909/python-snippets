class Vehicle:
    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.gas = 4  # Full tank

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print(f"The {self.color} {self.manufacturer} goes VROOOM!")
        else:
            print(f"The {self.color} {self.manufacturer} sputters out of gas")


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


class ECar(Car):
    def drive(self):
        print(f"The {self.color} {self.manufacturer} goes whoosh!")


my_ecar = ECar("white", "Nissan")
my_ecar.window()
my_ecar.radio()
my_ecar.drive()

# Access the lingering gas tank
print(my_ecar.gas)
