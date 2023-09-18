""" Sorting Friends into Sets """


# set of all friends
friends = {
    "Mark",
    "Rae",
    "Verne",
    "Richard",
    "Aaron",
    "David",
    "Bruce",
    "Garry",
    "Bill",
    "Connie",
    "Larry",
    "Jim",
    "Landon",
    "Dillon",
    "Frank",
    "Tom",
    "Kyle",
    "Katy",
    "Olivia",
    "Brandon",
}

# set of people who live in my zip code
zipcode = {
    "Jerry",
    "Elaine",
    "Cindy",
    "Verne",
    "Rudolph",
    "Bill",
    "Olivia",
    "Jim",
    "Lindsay",
    "Rae",
    "Mark",
    "Kramer",
    "Landon",
    "Newman",
    "George",
}

# set of people who play Munchkin
munchkins = {"Steve", "Jackson", "Frank", "Bill", "Mark", "Landon", "Rae"}

# set of Olivia's friends
olivia = {"Jim", "Amanda", "Verne", "Nestor"}

# choose just the friends who live nearby
local = friends.intersection(zipcode)
print(f"I have {len(local)} local friends:")
print(local)

# remove the Munchkin players
invite = local.difference(munchkins)
print(f"I have {len(invite)} friends to invite:")
print(invite)

# revise the friends to invite set
invite = invite.symmetric_difference(olivia)
print(f"My revise set has {len(invite)} friends:")
print(invite)

# See all attributes of set()
print("See all available of set()", dir(set))
