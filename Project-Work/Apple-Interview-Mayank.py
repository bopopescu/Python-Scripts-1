
import math

a = [8,2,3,4,0,5,6,0,7]
p = []
j = 0

for i in range(len(a)):
    if a[i] == 0:
        j += 1
    else:
        p.append(a[i])

for k in range(j):
    p.append(0)

print ("Array", sorted(p, reverse=True))
