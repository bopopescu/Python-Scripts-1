__author__ = 'pnagwekar'
import fileinput
import sys

with open("out3", "w") as f:
    print("this is written to out3", file=f)

with fileinput.input() as f_input:
    for line in f_input:
        print(line)