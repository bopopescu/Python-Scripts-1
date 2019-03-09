'''
Question£º
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
import math
loc=[0,0]
while True:
    action=input()
    if not action:
        break
    s=action.split(" ")

    if s[0] == "UP":
        loc[1] += int(s[1])
    elif s[0] == "DOWN":
        loc[1] -= int(s[1])
    elif s[0] == "RIGHT":
        loc[0] += int(s[1])
    elif s[0] == "LEFT":
        loc[0] -= int(s[1])
print (loc)

step = math.sqrt(int(loc[0]) ** 2 + (int(loc[1]) ** 2))
print(int(step))








