'''
def putnumers(n):
    s=[]
    i=1
    while i <= n:
        if i % 7 == 0:
            s.append(i)
        i+=1
    return(s)
print(putnumers(int(input())))

'''
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reverse(100):
    print (i)
