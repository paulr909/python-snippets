from abc import ABC, abstractmethod
from copy import deepcopy


class Prototype(ABC):
    def clone(self):
        pass


class Proto1Object(Prototype):
    def __init__(self, arg1, arg2):
        self.field1 = arg1
        self.field2 = arg2

    def __operation__(self):
        self.performed_operation = True

    def clone(self):
        obj = Proto1Object(self.field1, self.field2)
        obj.performed_operation = self.performed_operation
        return obj


# Alternatively, you can use the deepcopy function instead of simply assigning fields like in the previous example:


class Proto2Object(Prototype):
    def __init__(self, arg1, arg2):
        self.field1 = arg1
        self.field2 = arg2

    def __operation__(self):
        self.performed_operation = True

    def clone(self):
        return deepcopy(self)
