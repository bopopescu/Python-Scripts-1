l=[1,2,3,0,0,1]

l = [x for x in l if x]
print(l)

l=[1,2,3,0,0,1]
m=[]
for x in l:
    if x != 0:
        m.append(x)
print(m)

l=[1,2,3,0,0,1]
i =0
while i < len(l):
    if l[i] == 0:
        l.pop(i)
    else:
        i+=1
print(l)


