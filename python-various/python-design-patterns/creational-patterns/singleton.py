# Singleton design pattern
class Singleton:
    __shared_instance = "Paul Codes"

    def __init__(self):
        """Virtual private constructor"""
        if Singleton.__shared_instance != "Paul Codes":
            raise Exception("This class is a singleton class!")
        else:
            Singleton.__shared_instance = self

    @staticmethod
    def get_instance():
        """Static access method"""
        if Singleton.__shared_instance == "Paul Codes":
            Singleton()
        return Singleton.__shared_instance


# main method
if __name__ == "__main__":
    # Create object of Singleton Class
    obj = Singleton()
    print(obj)

    # Pick the instance of the class
    obj = Singleton.get_instance()
    print(obj)
    print(obj is Singleton.get_instance())
