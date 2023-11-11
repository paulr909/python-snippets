import abc


class MyABC(object):
    """Abstract Base Class Definition"""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def do_something(self, value):
        """Required method"""
        pass

    @property
    @abc.abstractmethod
    def some_property(self):
        """Required property"""
        pass


class MyClass(MyABC):
    """Implementation of MyABC"""

    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        """Implementation of abstract method"""
        self._myprop *= 2 + value

    @property
    def some_property(self):
        """Implementation of abstract property"""
        return self._myprop


a = MyClass(value=42)
print(a.some_property)
a.do_something(value=41)
print(a.some_property)
