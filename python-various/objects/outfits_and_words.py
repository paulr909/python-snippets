""" You Can Change an Outfit, But You Can't Change Your Words """

# Create a closet full of clothes
closet = ["shirt", "hat", "pants", "jacket", "socks"]
print(closet)
print(id(closet))

# Remove a hat
closet.remove("hat")
print(closet)
print(id(closet))

# Create a poor choice of words
words = "You're wearing that"
print(words)
print(id(words))

# Add more to the phrase
words = words + " because you look great!"
print(words)
print(id(words))
