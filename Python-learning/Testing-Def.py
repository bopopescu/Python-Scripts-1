__author__ = 'pnagwekar'

def Ask(prompt='', retries=10, complaints="Yes or No Please"):

    while True:
        ok=input("Please enter yes or no =")
        if ok in ("yes","y", "Y", "ye", "YE", "YES"):
            return True
        if ok in ("No", "no", "n","N"):
            return False
        retries=retries-1
        if retries < 0:
            print("You are very Uncooperative user")
        print(complaints)

m=Ask()
if m is True:
    print('You are deserved')
else:
    print("All the best for your future endeavor")