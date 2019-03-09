__author__ = 'pnagwekar'
import sys
play = 1
i = 0
a = list()
b = list()
while play:
    n = int(input("Please input number in Array: "))
    a.append(int(n))
    p = input("Do you want to enter more numbers (yes/no):  ")
    while p:
        if (p=="no") or (p=="n"):
            play=0
            break
        elif (p=="yes") or (p=="y"):
            i=i+1
            break
        else:
            p = input("Enter your choice as only (y,yes,n,no), please enter again:  ")
print ("Numbers that you entered:", a)
a.sort()
print ("Sorted",a)
a
a.reverse()
a
print ("Inverse Sorted",a)
for i in range(0,(len(a)-1),1):
    for j in range((i+1),len(a),1):
        if a[i] < a[j]:
            m=a[i]
            a[i]=a[j]
            a[j]=m
print ("Sorted Array:", a)