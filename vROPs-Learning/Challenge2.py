import requests
from requests.auth import HTTPBasicAuth
import pprint

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
p = requests.get('https://httpbin.org/get', params=payload)
print(p.text)
print(p.url)

r = requests.get("https://eso-vrops.eng.vmware.com/suite-api/api/resources", auth=HTTPBasicAuth('RestAdmin', 'Vmware1234!'), verify=False)
print(r.json())


