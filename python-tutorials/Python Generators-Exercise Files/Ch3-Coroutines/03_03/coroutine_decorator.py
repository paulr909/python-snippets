def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.__next__()
        return cr

    return wrap


@coroutine_decorator
def coroutine_example():
    while True:
        x = yield
        # do something with x
        print(x)


c = coroutine_example()
c.send('success!')

# error with above

# https://stackoverflow.com/questions/47120752/why-do-we-need-the-asyncio-coroutine-decorator