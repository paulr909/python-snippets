import os
import csv

path = "/home/paul/PycharmProjects/django-projects/all-web-xyz/contact/"

os.chdir(path)
from dashboard.models import Contact

with open("contacts.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        p = Contact(name=row["Name"], email=row["Email"], telephone=row["telephone"])
        p.save()

exit()
