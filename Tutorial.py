import urllib
import urllib.request
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

theurl = "https://umich.edu/"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

print (soup.title.text)

#FOLLOWING CODE FINDS ALL LINKS
#print (soup.findAll('a'))

#FOLLOWING CODE ORGANIZES ALL LINKS
"""
for link in soup.findAll('a'):
    print(link.get('href'))
    print(link.text)
"""

print(soup.title.text)
print(soup.findAll('a')[0])
print(soup.find('div', {"class": "ProfileHeaderCard"}))
