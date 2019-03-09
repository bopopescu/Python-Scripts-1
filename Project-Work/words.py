__author__ = 'pnagwekar'
name = input("Enter file name")
handle = open(name,'r')
text = handle.read()
words = text.split()
print (words)
counts = dict()
print (counts)
for word in words:
    counts[word]=counts.get(word,0) + 1
