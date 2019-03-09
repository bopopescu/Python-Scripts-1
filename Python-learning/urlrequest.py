import urllib.request
import urllib.parse

# Get the URL ready with query embedded. You need Parser for this
values = {'q': 'python programming tutorials'}
data = urllib.parse.urlencode(values)
url ='https://www.google.com/search?'+data

# test URL
print (url)

'''data = data.encode('utf-8')'''

# Pretend that you are Firefox
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

# In object oriented programming, you will use (self, *args, **kwargs).
# Request has R capitol. Tha means it's Class. headers is Keyword Arguments
# Let's send request with header as if you are firefox


req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
print(resp.read())