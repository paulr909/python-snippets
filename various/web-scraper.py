import urllib2
import re

# connect to a URL
website = urllib2.urlopen('http://www.bbc.co.uk/news')

# read html code
html = website.read()

# use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

print(links)
