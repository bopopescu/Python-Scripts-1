

try:
    x=5
    import parag
    print(x+"5")
except TypeError as t:
    print ("It's type error", t)
except NameError as n:
    print("It's name error")
except Exception as e:
    print ('General Exception', e)

while True:
    try:
        name = input("Please enter name")
        if name.isalnum():
            break
    except Exception as e:
        print("Please enter name in string")


print( "Great Job")

