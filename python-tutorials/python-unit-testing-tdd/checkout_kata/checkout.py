class Checkout:
    class Discount:
        def __init__(self, number_items, price):
            self.number_items = number_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_discount(self, item, number_of_items, price):
        discount = self.Discount(number_of_items, price)
        self.discounts[item] = discount

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_total(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculate_item_total(item, count)
        return total

    def calculate_item_total(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.number_items:
                total += self.calculate_item_discounted_total(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count

        return total

    def calculate_item_discounted_total(self, item, count, discount):
        total = 0
        number_of_discounts = count / discount.number_items
        total += number_of_discounts * discount.price
        remaining = count % discount.number_items
        total += remaining * self.prices[item]
        return total
