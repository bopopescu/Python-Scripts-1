import json
import requests

# Write File

data = [
        {"president1":
            {
            "name": "Parag Nagwekar",
            "species": "Betelgeusian",
            },
        "president2":
            {
            "name": "Barak Obama",
            "species": "Betelgeusian",
            }
        }
        ]

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)


# Read File

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
print(json.dumps(data, indent=4))

d={}
u={}
for item in data:
    for key in item:
        try:
            u[item[key]["name"]] +=1
        except KeyError:
            u[item[key]["name"]] = 1
print(u)