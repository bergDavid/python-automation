#Web Scraping: bs4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#url = input('Enter - ')
url = "http://wwww.dr-chuck.com/page1.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

#Retrive all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))