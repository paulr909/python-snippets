cheese = "cheddar"


def mix_and_cook():
    print("Mixing the ingredients")
    print("Greasing the frying pan")
    print("Pouring the mixture into a frying pan")
    print("Cooking the first side")
    print("Flipping it!")
    print("Cooking the other side")


def make_omelette():
    global cheese
    cheese = "swiss"
    mix_and_cook()
    omelette = f"A {cheese} omelette"
    return omelette


def make_pancake():
    mix_and_cook()
    pancake = f"A {cheese} pancake"
    return pancake


def fancy_omelette(*ingredients):
    mix_and_cook()
    omelette = f"A fancy omelette with {len(ingredients)} ingredients"
    return omelette


# make some cheesy foods
print(cheese)
print(make_omelette())
print(cheese)
print(make_pancake())
print(fancy_omelette("pineapple", "olives"))
