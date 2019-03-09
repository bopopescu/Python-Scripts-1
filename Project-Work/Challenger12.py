'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

r = input("Please enter your statement")
l=0
d=0
for i in r:
    if i.isalpha():
        l=l+1
    elif i.isdigit():
        d=d+1

print("Digits =", d)
print("letters =", l)