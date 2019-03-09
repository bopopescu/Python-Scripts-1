f = open("student.txt", mode="r")

l=[]
for lines in f:
    l.append(lines.split('^^^^'))

for i in range(len(l)):
    for j in range (i,len(l)):
        if l[i][2] < l[j][2]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(l)
