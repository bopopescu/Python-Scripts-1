
import math
import statistics
studentdict = {}

def enterGrades():
    print("\n======Entering Grades======\n")
    name=input("Please enter name of the students ---> ")
    grade=input("Please enter grade ---> ")
    if name in studentdict:
        studentdict[name].append(float(grade))
    else:
        studentdict[name] = [float(grade)]
    print(studentdict)
'''    while True:
        grade = [int(x) for x in input().split()]
        if (len(grade) == 3):
            break
        else:
           print(" Please enter 3 values for grades. Please try again ")
'''

def removeStudent():
    print("\n=====Removing Students======\n")
    name = input("Please enter name of the students --->  ")
    try:
        del studentdict[name]
    except Exception as e:
        print("\n Student not found \n")
    print(studentdict)

def averageGrades():
    print("\n======Averaging Grades======\n")
    name = input("Please enter name of the students ---> ")
    try:
        avg = statistics.mean(studentdict[name])
        print("\nAverage of", name, "is", avg)
    except Exception as e:
        print("\nStudent not found. Please check and try again \n")

def main():

    while True:
        print( "\nWelcome to Grade Central\n")
        print(" [1] Enter Grades\n")
        print(" [2] Remove Student\n")
        print(" [3] Student Average Grades\n")
        print(" [4] Exit\n")

        n = input("Please enter it here -->  ")
        if (n == "1"):
            enterGrades()
        elif (n == "2"):
            removeStudent()
        elif(n== "3"):
            averageGrades()
        elif (n == "4"):
            print (studentdict)
            break
        elif ():
            print("Please enter choice from 1 to 4")


if __name__ == '__main__':
    main()

