#!/usr/bin/env python

import math

def main():
    sales_record=(300,200,300,200)
    while True:
        try:
            recent= int(input("Enter your numbers for this quarter:-- "))
            break
        except:
            print ("Please enter numbers")
    lastaverage = sum(sales_record)/len(sales_record)
    if recent > lastaverage:
        print ("****Aahana, you were exceptional sales person last quarter. Keep doing your job ****\n ")
    else:
        print ("Try harder. Better luck next time \n")
    while True:
        try:
            p = int(input("Please enter the NUMBER for square root here :-- "))
            break
        except:
            print ("Not valid number")
    s = math.sqrt(p)
    print ("Your Number is", p)
    print ("Square root of", p, "is", s)
    name = input("Type aahana to continue")
    while name != "aahana":
        name = input ("Please type aahana. Try again --")
    while True:
        try:
            j = int(input("Please enter any number than we want to repeat till 1000 --y :-- "))
            break
        except:
            print ("Not valid number")
    while j > 1000:
        j = int(input ("Please type number less than 1000. Try again --"))
    k = 0
    for i in range(j,1001,j):
            print(i)
            k = k+1
    print (" it counted",k, "times")

# start this thing
if __name__ == "__main__":
    main()