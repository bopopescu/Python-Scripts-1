def QuestionsMarks(str):
    a,b = 0,0
    x = 'false'

    for i in range(len(str)-1):
        for j in range(i,len(str)):
            if str[i].isdigit() and str[j].isdigit() and int(str[i]) + int(str[j]) == 10:
                a,b = i,j
                print (a,b)
                new = s[a+1:b+1]
                if new.count('?') == 3:
                    print(s[i:j + 1])
                    x = 'true'
                    break
    return(x)



s = input("Please enter the string")
print (QuestionsMarks(s))