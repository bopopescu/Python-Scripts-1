from operator import itemgetter

test =  {'2', '1', '3'}
s = ', '
print (test)
print(s.join(test))

test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))

test = {'mat': 1, 'that': 2}
s = '->'
print(s.join(test))

test = {1:'mat', 2:'that'}
s = ', '


# this gives error
try:
    print(s.join(test))
except:
    print ("Can't work on values")

student_tuples=[('jane', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10), ('dave', 'B', 20)]
student_tuples=sorted(student_tuples, key=itemgetter(0,1,2), reverse=True)
print(student_tuples)