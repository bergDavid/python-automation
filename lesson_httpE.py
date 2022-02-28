#Web Browser: urllib
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://www.dr-chuck.com/page1.htm"
url = "https://www.si.umich.edu/"
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,"html.parser")

#Retrive all of the anchors tags
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))