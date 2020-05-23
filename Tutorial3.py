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

soup = make_soup("https://www.tripadvisor.com/Hotel_Review-g297605-d8744366-Reviews-Seashell_Suites_and_Villas-Candolim_Bardez_North_Goa_District_Goa.html#REVIEWS")
link = soup.find(attrs={"class": "ui_pagination is-centered"})
print(link.get('href'))
