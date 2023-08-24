collection = [
    "Adam",
    "Anne",
    "Barry",
    "Brianne",
    "Charlie",
    "Cassandra",
    "David",
    "Dana",
]

# list comprehension
new_list = [item.upper() for item in collection]
print(new_list)

# generator expression assigned to a variable
upper_names = (item.upper() for item in collection)

# then call list method with upper_names as an argument
print(list(upper_names))
