__author__ = 'pnagwekar'
import requests
import json

vROPs_url = "https://eso-monitor.eng.vmware.com/suite-api/api/adapters"

'''
data = json.dumps({'name':'test', 'description':'some test repo'})
'''
r = requests.get(vROPs_url, auth=('admin', 'Ca$hc0w1'), verify=False)
print (r.json())
