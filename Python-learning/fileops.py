from class1 import calc
writeme = "Example Text"

savefile = open ("parag.txt", 'a')
savefile.write(writeme)
savefile.write('\n')
savefile.write("Just appending")
savefile.write('\n')
savefile.close()

# readfile and create list with line by line
readfile = open ("parag.txt", 'r').readlines()
print(readfile)

# readfile but split every word
readfile = open ("parag.txt", 'r').read()
print(readfile.split('\n'))


a=20
b=10

print(calc.add(a,b))
print(calc.substract(a,b))
print(calc.multi(a,b))
print(calc.div(a,b))