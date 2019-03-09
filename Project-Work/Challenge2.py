'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
'''

def fact(n):
    if (n == 0):
        return 1
    else:
        return (n*fact(n-1))

n = int(input("Please enter your number"))
print ("factorial of f is --->", fact(n))