# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


# then call it by using a list method
print(list(even_integers_generator(10)))
