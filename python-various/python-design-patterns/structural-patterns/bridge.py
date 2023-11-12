from abc import ABC, abstractmethod


class Material(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Cobblestone(Material):
    def __init__(self):
        pass

    def __str__(self):
        return "cobblestone"


class Wood(Material):
    def __init__(self):
        pass

    def __str__(self):
        return "wood"


class Building(ABC):
    @abstractmethod
    def print_name(self):
        pass


class Tower(Building):
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def print_name(self):
        print(str(self.material) + " tower " + self.name)


class Mill(Building):
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def print_name(self):
        print(str(self.material) + " mill " + self.name)


if __name__ == "__main__":
    cobb = Cobblestone()
    local_mill = Mill("Hilltop Mill", cobb)
    local_mill.print_name()

    wooden = Wood()
    watchtower = Tower("Abandoned Sentry", wooden)
    watchtower.print_name()
