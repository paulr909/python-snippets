from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def calculate_risk(self):
        pass


class Employed(Product):
    def __init__(self, name, age, hours):
        self.name = name
        self.age = age
        self.hours = hours

    def calculate_risk(self):
        # Please imagine a more plausible implementation
        return self.age + 100 / self.hours

    def __str__(self):
        return self.name + " [" + str(self.age) + "] - " + str(self.hours) + "h/week"


class Unemployed(Product):
    def __init__(self, name, age, able):
        self.name = name
        self.age = age
        self.able = able

    def calculate_risk(self):
        # Please imagine a more plausible implementation
        if self.able:
            return self.age + 10
        else:
            return self.age + 30

    def __str__(self):
        if self.able:
            return self.name + " [" + str(self.age) + "] - able to work"
        else:
            return self.name + " [" + str(self.age) + "] - unable to work"


class PersonFactory:
    def get_person(self, type_of_person):
        if type_of_person == "employed":
            return Employed("Oliver", 22, 30)
        if type_of_person == "unemployed":
            return Unemployed("Sophie", 33, False)


if __name__ == "__main__":
    factory = PersonFactory()

    product = factory.get_person("employed")
    print(product)

    product2 = factory.get_person("unemployed")
    print(product2)
