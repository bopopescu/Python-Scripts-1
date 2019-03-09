
'''
[1,2,4,3,3,5],6
'''


def pair(array,k):
    a=[]
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] + array[j] == k and array[i] not in a:
                a.append(array[i])
                a.append(array[j])
                print(array[i], array[j])
                continue
    return(a)

b = [1,2,4,3,3,5,5,6,9,10,12,11,10,14,13]
l = 15
c = pair(b,l)
print(c)