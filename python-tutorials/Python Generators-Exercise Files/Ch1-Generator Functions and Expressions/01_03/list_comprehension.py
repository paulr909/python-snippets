collection = ['Adam', 'Anne', 'Barry', 'Brianne', 'Charlie', 'Cassandra', 'David', 'Dana']

# list comprehension
newlist = [item.upper() for item in collection]

# generator expression
(item.upper() for item in collection)

# assign to a variable
upper_names = (item.upper() for item in collection)

# then call list method with upper_names as an argument
list(upper_names)
