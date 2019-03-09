import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.urlopen('https://finance.yahoo.com')
xml = BeautifulSoup(req, 'xml')

for item in xml.findAll('link')[1:]:
    print(item)


