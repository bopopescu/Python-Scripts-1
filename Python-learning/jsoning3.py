data = [
        {
            "name": "Parag Nagwekar",
            "age": "42",
            "sex": "M",
            "species": "Indian",
        },
        {
            "name": "Barak Obama",
            "age": "45",
            "sex": "M",
            "species": "Hawaain",
        },
        {
            "name": "Michelle Obama",
            "age": "41",
            "sex": "F",
            "species": "American",
        },
        {
            "name": "Sean Obama",
            "age": "22",
            "sex": "M",
            "species": "American",
        }
        ]

import json
from operator import itemgetter

# Sort by Male and then Female
m=[]
f=[]
for item in data:
        if item["sex"] == "M":
            m.append(item)
        else:
            f.append(item)
for item in f:
    m.append(item)
print(json.dumps(m, indent=4))

# Find only American
a=[]
for item in data:
    if item["species"] == "American":
        a.append(item)
print("\n\n*****Members of American******")
print(json.dumps(a,indent=4))

# Find members of Obama Family
o=[]
for item in data:
    lastname=item["name"].split(" ")
    if lastname[1] == "Obama":
        o.append(item)
print("\n\n*****Members of Obama Family******")
print(json.dumps(o,indent=4))

# Sort the list by Age
newlist=sorted(data, key=itemgetter('age'), reverse=True)
print(json.dumps(newlist,indent=4))


