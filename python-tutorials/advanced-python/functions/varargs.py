# Demonstrate the use of variable argument lists


# define a function that takes variable arguments
def addition(base, *args):
    result = 0
    for arg in args:
        result += arg

    return result


def main():
    # pass different arguments
    print(addition(5, 10, 15, 20))
    print(addition(1, 2, 3))

    # pass an existing list
    nums = [5, 10, 15, 20]
    print(addition(*nums))


if __name__ == "__main__":
    main()
