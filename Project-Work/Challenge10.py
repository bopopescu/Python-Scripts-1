# Find index of min

'''
li = input("Please input your values separated by , ----> ")
l = [int(x) for x in li.split(',')]
index=0
for i in range(len(l)):
    if l[i] < l[index]:
        index=i

print("index is -->", index)


Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''

bin=input("Please inout your binary numbers by , ---> ")
b = [x for x in bin.split(',')]
value=[]
for p in b:
    intp = int(p, 2)
    print (intp)
    if not intp % 5:
       value.append(p)

print (','.join(value))