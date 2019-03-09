__author__ = 'pnagwekar'


class example():

    def __init__(self, *args, **kwargs):

        self.color = input("Please give me your color---> ")
        self.size = input("Please give me your size---> ")

    def setnumber(self):
        self.number=12
    def setpart(self):
        self.part='z'
    def getsize(self):
        return '{}', format(self.size)
    def getcolor(self):
        return self.color


p=example()
p.setnumber()
p.setpart()
p1=example()

print(p.color)
print(p.size)
print(p.number)
print(p.part)
print(p1.color)
print(p1.size)





