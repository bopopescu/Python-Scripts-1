from urllib import Request, urlopen, URLError

request = Request('hhtp://placekitten.com/')

try:
    response = urlopen(request)
    kittens = response.read()
    print kittens[559:1000]
except URLError, e:
        print 'No Kittez, Got an error code:', e
