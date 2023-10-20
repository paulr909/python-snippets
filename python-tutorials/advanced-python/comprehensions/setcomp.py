# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    c_temps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # build a set of unique Fahrenheit temperatures
    f_temps1 = [(t * 9 / 5) + 32 for t in c_temps]
    f_temps2 = {(t * 9 / 5) + 32 for t in c_temps}
    print(f_temps1)
    print(f_temps2)

    # build a set from an input source
    f_temps2 = "The quick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in f_temps2 if not c.isspace()}
    print(chars)


if __name__ == "__main__":
    main()
