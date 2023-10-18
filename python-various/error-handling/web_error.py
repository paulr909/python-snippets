""" Trying to download things that don't exist """

import urllib.request

try:
    webpage = urllib.request.urlopen("http://www.google.com")
except Exception as e:
    print(e)
    print("Could not access webpage!")
else:
    for line in webpage:
        print(line)
