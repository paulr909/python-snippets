# Customize string representations of objects


class Person:
    def __init__(self):
        self.first_name = "Lucy"
        self.last_name = "verasamy"
        self.age = 43

    # Use __repr__ to create a string useful for debugging
    def __repr__(self):
        return f"<Person Class - first_name:{self.first_name}, last_name:{self.last_name}, age:{self.age}>"

    # Use str for a more human-readable string
    def __str__(self):
        return f"Person ({self.first_name} {self.last_name}, {self.age})"

    # Use bytes to convert the informal string to a bytes object
    def __bytes__(self):
        val = f"Person:{self.first_name}:{self.last_name}:{self.age}"
        return bytes(val.encode("utf-8"))


def main():
    # Create a new Person object
    cls1 = Person()

    print(repr(cls1))
    print(str(cls1))
    print(f"Formatted: {cls1}")
    print(bytes(cls1))


if __name__ == "__main__":
    main()
