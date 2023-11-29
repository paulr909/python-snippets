# Give objects number-like behavior


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point x:{self.x},y:{self.y}"

    # Implement addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Implement subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Implement in-place addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


def main():
    # Declare points
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    # Add two points
    p3 = p1 + p2
    print(p3)

    # Subtract two points
    p4 = p2 - p1
    print(p4)

    # Perform in-place addition
    p1 += p2
    print(p1)


if __name__ == "__main__":
    main()
