class Dog:
    def __init__(self, name):
        self.name = name

    def sit(self):
        print(f"{self.name} is sitting")


my_dog = Dog("Shaggy")
print(f"{my_dog.name} is a great dog!")
my_dog.sit()


class SearchDog(Dog):
    def __init__(self, name):
        super().__init__(name)

    def search(self):
        print(f"{self.name} is searching")


my_dog = SearchDog("Snoop")
print(f"{my_dog.name} is a search dog")
my_dog.sit()
my_dog.search()
