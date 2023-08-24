cowboy = {"age": 32, "horse": "mustang", "hat_size": "large"}
if "name" in cowboy:
    name = cowboy["name"]
else:
    name = "The Man with No Name"

print(name)

name_v2 = cowboy.get("name", "The Man with No Name")

print(name_v2)

# if not in
if "name" not in cowboy:
    cowboy["name"] = "The Man with No Name"

name_v3 = cowboy["name"]

print(name_v3)

name_v4 = cowboy.setdefault("name", "The Man with No Name")

print(name_v4)
