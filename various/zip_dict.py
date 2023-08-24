import json

a = ["username", "first name", "last name"]
b = [["user1", "Jack", "Dawson"], ["user2", "Roger", "Federer"]]

print(json.dumps([dict(zip(a, row)) for row in b], indent=1))
