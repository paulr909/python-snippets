# using generators to find the longest name

full_names = (name.strip() for name in open("names.txt"))
lengths = ((name, len(name)) for name in full_names)
longest = max(lengths, key=lambda x: x[1])

# use above with
print(longest)
# or with
print(list(longest))
