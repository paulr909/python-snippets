class Dog:
    def __init__(self, name):
        """Initialize dog object."""
        self.name = name

    def sit(self):
        """Simulate sitting."""
        print(f"{self.name} is sitting.")


my_dog = Dog("Peso")
print(f"{my_dog.name} is a great dog!")
my_dog.sit()


class SearchDog(Dog):
    """Represent a search dog."""

    def __init__(self, name):
        """Initialize the search dog."""
        super().__init__(name)

    def search(self):
        """Simulate searching."""
        print(f"{self.name} is searching.")


my_dog = SearchDog("Willie")
print(f"{my_dog.name} is a search dog.")
my_dog.sit()
my_dog.search()
