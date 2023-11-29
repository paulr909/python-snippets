""" Two Names, One Shirt """


class Shirt:
    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True


# Create one shirt with two names
red = Shirt()
crimson = red

# Examine the red/crimson shirt
print(id(red))
print(id(crimson))
print(red.clean)
print(crimson.clean)

# Spill juice on the red/crimson shirt
red.make_dirty()
print(red.clean)
print(crimson.clean)

# Check that red and crimson are the same shirt
print(red is crimson)

# Create a second shirt to be named crimson
crimson = Shirt()

# Examine both shirts
print(id(red))
print(id(crimson))
print(crimson.clean)
print(red.clean)

# Clean the red shirt
red.make_clean()
print(red.clean)
print(crimson.clean)

# Check that red and crimson are different shirts
print(red is crimson)
