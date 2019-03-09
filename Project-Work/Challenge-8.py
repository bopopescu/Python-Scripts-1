'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

listofwords=input("Your list of word separated by , ---->")
words=listofwords.split(',')
words.sort()
print(','.join(words))

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

lines=[]
while True:
    line=input("Your String here and press enter. Once done, please press enter ----> ")
    if line:
       lines.append(line)
    else:
        break

for line in lines:
    print(line.upper())
