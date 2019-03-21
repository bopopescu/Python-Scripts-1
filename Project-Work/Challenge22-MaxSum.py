import re
'''
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345, qawsedrf123#, qawsed123@,Qawsr123@
Then, the output of the program should be:
ABd1234@1

# Following is the solution 
pwd = input("Please enter you password")
pwdlist=pwd.split(",")
for i in pwdlist:
    if len(i) < 6 or len(i) > 12:
        print("Incorrect lenght. It should be between 6 to 12 charactoer long")
        continue
    elif re.search("[A-Z]", i) and re.search("[#@!]", i) and re.search("[a-z]", i) and re.search("[0-9]", i):
        print(i)
'''

while True:
    pwd = input("Please enter you password or just press ENTER to stop")
    if len(pwd) == 0:
        break
    elif len(pwd) < 6 or len(pwd) > 12:
        print("Incorrect lenght. It should be between 6 to 12 charactoer long")
    elif re.search("[A-Z]", pwd) and re.search("[#@!]", pwd) and re.search("[a-z]", pwd) and re.search("[0-9]", pwd):
        print("Great Job")
    else:
        print("Password should have one Upper, one lower, one digit and one special character")