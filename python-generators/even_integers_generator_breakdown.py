# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


# assign to a variable
integers = even_integers_generator(10)

# then call it by using the next method
integers.next()
# above only works in python2.7

# for python3 use below
integers.__next__()
# calling next() on exhausted generator raises StopIteration

# or use the generator object in a for loop
for n in integers:
    print(n)

# or use the generator expression in a for loop, for loop will handle the StopIteration
for n in (i for i in range(10)):
    print(n)

# find max value
max((i for i in range(10)))

# only one set of parenthesis
max(i for i in range(10))
