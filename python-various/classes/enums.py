# Define enumerations using the Enum base class

from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()


def main():
    # Enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # Enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # Print the auto-generated value
    print(Fruit.PEAR.value)

    # Enums are hashable, can be used as keys
    my_fruits = {}
    my_fruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(my_fruits[Fruit.BANANA])


if __name__ == "__main__":
    main()
