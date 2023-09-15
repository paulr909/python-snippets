# Enumerate over a list of items
fruits = ["apple", "banana", "cherry"]

for fruit in enumerate(fruits):
    print(fruit)

# Enumerate over a tuple of items with start index of 1
colours = ("red", "green", "blue", "yellow", "orange", "purple")

for index, colour in enumerate(colours, start=1):
    print(index, colour)

# Enumerate over a dictionary
person = {"name": "John", "age": 30, "city": "New York"}

for index, (key, value) in enumerate(person.items()):
    print(index, key, value)
