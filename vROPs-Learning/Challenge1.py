
import nagini
import rlcompleter, readline
import optparse
import pprint
import json


print ("Connecting to vROps")
readline.parse_and_bind('tab:complete')
vcops = nagini.Nagini(host="eso-vrops.eng.vmware.com", user_pass=("RestAdmin", "Vmware1234!"))
print ("Completed")

with open ("resource.txt", "w") as writefile:
    for resource in vcops.get_resources(resourceKind="VirtualMachine")['resourceList']:
        print(resource['resourceKey']['name'])

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(vcops.get_solution())

print(resource['identifier'], resource['resourceKey']['name'])
