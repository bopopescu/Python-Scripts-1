'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

string = input("Please enter your numbers separated by ,")
names=string.split(',')
names.sort()
print(names)
print(",".join(names))
'''

from array import *

def main ():
    x = int(input("Please enter your number X here ->"))
    y = int(input("Please enter your number Y here ->"))
    t = [[0 for j in range(y)] for i in range(x)]
    print(t)

    for i in range(x):
        for j in range(y):
            t[i][j] = i*j
    print(t)

if __name__ == '__main__':
    main()