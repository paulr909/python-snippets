def mix_and_cook():
    print("Mixing the ingredients")
    print("Greasing the frying pan")
    print("Pouring the mixture into a frying pan")
    print("Cooking the first side")
    print("Flipping it!")
    print("Cooking the other side")


def make_omelette(ingredient):
    mix_and_cook()
    omelette = f"a {ingredient} omelette"
    return omelette


def make_pancake():
    mix_and_cook()
    pancake = "a delicious pancake"
    return pancake


def fancy_omelette(*ingredients):
    mix_and_cook()
    omelette = f"a fancy omelette with {len(ingredients)} ingredients"
    return omelette


# make some regular omelettes
print(make_omelette("bacon"))
print(make_omelette("spam"))

# make Olivia's fancy omelette
print(fancy_omelette("onion", "pepper", "spinach", "mushroom", "tomato", "goat cheese"))
