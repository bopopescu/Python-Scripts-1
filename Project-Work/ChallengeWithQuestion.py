s = input()
questionmark=0
ans =False
for t in s:
    if t.isdigit():
        print(t)
        if questionmark < 3:
            value1=int(t)
        else:
            value2 = int(t)
            if (value1+value2) == 10:
               ans = True
               print(value1, value2, ans, questionmark)
               break
            else:
                questionmark=0
    elif t =="?":
        questionmark+=1
print(ans)

'''
def QuestionsMarks(s): 
    questionmark=0
    ans ='false'
    for t in s:
        if t.isdigit():
            if questionmark < 3:
                value1=int(t)
            else:
                value2 = int(t)
                if (value1+value2) == 10:
                   ans = 'true'
                   return(ans)
                else:
                    questionmark=0
        elif t =="?":
            questionmark+=1
    return(ans)
print QuestionsMarks(input())
'''