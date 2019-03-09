'''
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''


ID = 0

while True:
    t = input("Do you want to continue? -->")
    if (t == "y") or (t == "yes") or (t == "Y"):
        tr=input("Please enter D for Deposit, W for Withdrawl and then amount e.g. D 100 or W 100 -->")
        trans=tr.split(" ")
        if trans[0] == "D":
            ID = ID + int(trans[1])
        elif trans[0] == "W":
            ID = ID - int(trans[1])
    else:
        print ("Total amount -->", ID)
        break




