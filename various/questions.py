import sys
import random
import datetime

remarks = [
    "Isn't it a nice day!",
    "How are you today?",
    "I hear there was another shooting",
]
reply = ["Really?", "Oh wow!", "Yeah...", "Cool!"]

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("Please tell me your name: ")
    if name == "":
        name = "Monty"

hour = datetime.datetime.now().hour

if hour < 12:
    print("Good morning", name)
elif hour < 18:
    print("Good afternoon", name)
else:
    print("Good evening", name)

input(random.choice(remarks))
print(random.choice(reply), "Oh well, see you later!\n")
