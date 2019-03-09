__author__ = 'pnagwekar'
array=['hey','how', 'are','you']
print (array)
array.insert(4,'Jain')
array.insert(5,'how')
for i in range (0, len(array),1):
    array[i]=array[i].upper()
    if ("HOW" in array[i]):
        print("great", array[i])
print (array.pop(0))
print (array.count('HOW'))
len(array)
print(array)


