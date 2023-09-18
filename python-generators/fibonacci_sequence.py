# Fibonacci sequence generator
def fibonacci_gen():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


for index, x in enumerate(fibonacci_gen()):
    if index == 10:
        break
    print(f"Index: {index}, Value: {x}")
