def num_generator(n: int):
    value = 0
    while value < n:
        yield value
        value += 1


# Iterate over the generator object produced by num_generator
for val in num_generator(3):
    print(val)


def squared(n: int):
    for i in range(n):
        yield i * i


for sqr in squared(5):
    print("gen v2:", sqr)
