'''
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

s = input("Please give me your sentence -->")
l=0
u=0

for g in s:
    if g.islower():
        l+=1
    elif g.isupper():
        u+=1

print ("UPPER CASE ", u)
print ("LOWER CASE ", l)


