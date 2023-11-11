class Singleton:
    __instance__ = None

    def __init__(self):
        """Constructor"""
        if Singleton.__instance__ is None:
            Singleton.__instance__ = self
        else:
            raise Exception("You cannot create another Singleton class")

    @staticmethod
    def get_instance():
        """Static method to fetch the current instance"""
        if not Singleton.__instance__:
            Singleton()
        return Singleton.__instance__


if __name__ == "__main__":
    # Create object of Singleton Class
    obj = Singleton()
    print(obj)

    # Pick the instance of the class
    obj = Singleton.get_instance()
    print(obj)
    print(obj is Singleton.get_instance())

    # This will cause an exception
    # new = Singleton()
    # print(new)
