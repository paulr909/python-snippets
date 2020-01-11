# Fibonacci Sequence Generator
def fibonacci_gen():
    trailing, lead = 0, 1
    while True:
        yield lead
        trailing, lead = lead, trailing + lead


# use with __next__()
fib = fibonacci_gen()

fib.__next__()

# use generator in a for loop
for _ in range(10):
    fib.__next__()
