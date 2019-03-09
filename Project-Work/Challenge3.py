'''
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
'''


def square(n):
    d = {}
    for i in range (1,n+1):
        d[i] = i*i
    return d

n =int(input("Please enter your last number"))
d = square(n)
print ("Square of numbers", d)