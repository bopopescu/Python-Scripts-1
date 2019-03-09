'''
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
'''

num = input("Please enter numbers")
a = num.split(',')
count = a.count('55')
f = num.find('55')

print ('tuple =', tuple(a))
print ('list =', a)
print ("count of 55 =", count)
print ("find of 55 = at", f)

