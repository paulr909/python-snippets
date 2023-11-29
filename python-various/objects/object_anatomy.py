""" What Makes Up an Object? """

# Examine a string object
print("shirt")
print(type("shirt"))
print(dir("shirt"))

# Use upper method on a string object
print("shirt".upper())

# Examine IDs of different string objects
print(id("shirt"))
print(id("pants"))

# Examine an integer object
print(id(1))
print(dir(1))

# Examine ID and attributes of functions
print(id(id))
print(dir(dir))
