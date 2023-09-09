# Example of adding a text encoding to existing file-like object

import urllib.request
import io
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

u = urllib.request.urlopen("https://www.python.org/")
f = io.TextIOWrapper(u, encoding="utf-8")
text = f.read()

print(text)
