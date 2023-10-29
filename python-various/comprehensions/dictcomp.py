# Demonstrate how to use dictionary comprehensions


def main():
    # define a list of temperature values
    c_temps = [0, 12, 34, 100]

    # Use a comprehension to build a dictionary
    temp_dict = {t: (t * 9 / 5) + 32 for t in c_temps if t < 100}
    print(temp_dict)
    print(temp_dict[12])

    # Merge two dictionaries with a comprehension
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Mackie": 88, "Pearce": 4}
    new_team = {k: v for team in (team1, team2) for k, v in team.items()}
    print(new_team)


if __name__ == "__main__":
    main()
