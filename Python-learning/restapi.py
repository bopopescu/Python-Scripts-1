#!/usr/bin/env python
import getopt, sys, os, errno
import requests
import json
import getpass
from requests.auth import HTTPBasicAuth

# Open http://placekitten.com/ for reading on line 4!
user="admin"
# passwd = getpass.getpass('Password:')
passwd="Vmware60!"
r = requests.get('https://vcopsqe-monitor-2.eng.vmware.com/suite-api/api/adapters', verify=False, auth=HTTPBasicAuth(user,passwd))
# Add your 'print' statement here!
print (r.status_code)
print (r.headers['content-type'])
print (r.encoding)
print (r.headers['server'])
print (r.content)