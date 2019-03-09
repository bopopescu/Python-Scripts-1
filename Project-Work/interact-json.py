import json

data = [{"Name": "Parag",
        'LastName': 'Nagwekar',
        'Age': '45',
        'Grade': '16',
        },
        {"Name": "Roopam",
        "LastName": "Jain",
        "Age": "45",
        "Grade": "16",
        },
        {"Name": "Aahana",
        "LastName": "Nagwekar",
        "Age": "10",
        "Grade": "4",
        }]


with open("file.txt", "w") as write_file:
    json.dump(data, write_file, indent=4)


with open("file.txt", "r") as read_file:
    data1 = json.load(read_file)

print(json.dumps(data1, indent=4))

d={}

for item in data1:
    if item['LastName'] == "Nagwekar":
        d = item
        print(item)