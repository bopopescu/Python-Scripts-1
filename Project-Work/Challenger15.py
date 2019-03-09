'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''

a = input("Please enter your number-->")
n1 = int("%s" % a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
n4 = int("%s%s%s%s" % (a,a,a,a))
p=n1+n2+n3+n4
print(p)

'''
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''

i = input("Please enter your numbers separated by , ")
k=[]
for t in i.split(','):
    if int(t)%2:
        k.append(t)

print(",".join(k))


