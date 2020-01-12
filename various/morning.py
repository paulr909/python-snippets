import datetime

hour = datetime.datetime.now().hour
name = input("Please tell me your name: ")

if hour < 12:
    print("Good morning", name)
elif hour < 18:
    print("Good afternoon", name)
else:
    print("Good evening", name)

print("You're wonderful!")
