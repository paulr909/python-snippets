import urllib
from PIL import Image
 
catapi="http://thecatapi.com/api/images/get?format=xml&results_per_page=1"
response = urllib.request.urlopen(catapi, timeout = 5)
imgurl = response.read().split()[6][5:-6].decode("utf-8")
Image.open(urllib.request.urlopen(imgurl, timeout = 5)).show()
