'''
Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''

from operator import itemgetter, attrgetter

def sortfirst(val):
    return val[0]

list=[]
while True:
    s=input()
    if s:
        list.append(tuple(s.split(",")))
    else:
        break

print(list)
list = sorted(list, key=sortfirst)

'''
for i in range(len(list)):
    for j in range(i,len(list)):
        if list [j][0] < list[i][0]:
            tmp = list[j]
            list[j] = list[i]
            list[i] = tmp
'''
for i in range(len(list)):
    for j in range(i,len(list)):
        if list [j][0] == list[i][0] and int(list [j][1]) < int(list[i][1]):
            tmp= list[j]
            list[j] = list[i]
            list[i] = tmp

for i in range(len(list)):
    for j in range(i,len(list)):
        if list[j][0] == list[i][0] and int(list[j][1]) < int(list[i][1]) and int(list [j][2]) < int(list[i][2]):
            tmp= list[j]
            list[j] = list[i]
            list[i] = tmp

print (list)
print(sorted(list, key=itemgetter(0,1,2)))