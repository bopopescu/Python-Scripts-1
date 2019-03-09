'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''


class inputoutstring(object):
    def __init__(self):
         self.s=""

    def getstring(self):
        self.s=input("Please give us your string")
        return(self.s)

    def printstring(self):
        print("Here is your string %s" %self.s)

if __name__ == '__main__':
    p=inputoutstring()
    p.getstring()
    p.printstring()

