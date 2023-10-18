specials = {
    "Sunday": "spinach",
    "Monday": "mushroom",
    "Tuesday": "pepperoni",
    "Wednesday": "veggie",
    "Thursday": "bbq chicken",
    "Friday": "sausage",
    "Saturday": "Hawaiian",
}


def order(day):
    pizza = specials[day]
    print(f"Order the {pizza} pizza")


# order the Saturday special!
order("Saturday")
