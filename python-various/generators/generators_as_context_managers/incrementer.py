# increments some_property by 1
from contextlib import contextmanager


@contextmanager
def simple_context_manager(obj):
    try:
        obj.some_property += 1
        yield
    finally:
        obj.some_property -= 1


class SomeObject(object):
    def __init__(self, arg):
        self.some_property = arg


# use with
obj = SomeObject(5)


with simple_context_manager(obj):
    print(obj.some_property)
