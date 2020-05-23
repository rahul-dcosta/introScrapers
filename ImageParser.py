import urllib
import urllib.request
from bs4 import BeautifulSoup
import ssl
import os
from string import ascii_lowercase

ssl._create_default_https_context = ssl._create_unverified_context

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

i = 1
soup = make_soup("https://umich.edu")
for img in soup.findAll('img'):
    temp = img.get("src")
    if temp[:1]=="/":
        image = "https://umich.edu" + temp
    else:
        image = temp

    nametemp = img.get('alt')
    if len(nametemp) == 0:
        filename=str(i)
        i=i+1
    else:
        filename=nametemp

    imagefile = open(filename + ".jpeg", 'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()
