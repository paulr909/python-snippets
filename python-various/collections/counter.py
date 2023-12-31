# Demonstrate the usage of Counter objects

from collections import Counter


def main():
    # list of students in class 1
    students_class_1 = [
        "Bob",
        "James",
        "Chad",
        "Darcy",
        "Penny",
        "Hannah",
        "Kevin",
        "James",
        "Melanie",
        "Becky",
        "Steve",
        "Frank",
    ]

    # list of students in class 2
    students_class_2 = [
        "Bill",
        "Barry",
        "Cindy",
        "Debbie",
        "Frank",
        "Gabby",
        "Kelly",
        "James",
        "Joe",
        "Sam",
        "Tara",
        "Ziggy",
    ]

    # Create a Counter for students_class_1 and class2
    c1 = Counter(students_class_1)
    c2 = Counter(students_class_2)

    # How many students in class 1 named James?
    print(c1["James"])

    # How many students are in class 1?
    print(sum(c1.values()), "students in class 1")

    # Combine the two classes
    c1.update(students_class_2)
    print(sum(c1.values()), "students in class 1 and 2")

    # What's the most common name in the two classes?
    print("Most common name:", c1.most_common(3))

    # Separate the classes again
    c1.subtract(students_class_2)
    print(c1.most_common(1))

    # What's common between the two classes?
    print(c1 & c2)


if __name__ == "__main__":
    main()
