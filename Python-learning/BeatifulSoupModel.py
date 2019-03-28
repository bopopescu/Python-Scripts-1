from bs4 import BeautifulSoup
import urllib.request

# req = urllib.request.urlopen('https://www.cnet.com/news')

with open ("Testing1.html", 'r') as req:
    xml = BeautifulSoup(req, 'xml')
    for item in xml.findAll('head'):
        print(item)
        print(50*'#')