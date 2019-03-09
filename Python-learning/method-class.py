__author__ = 'pnagwekar'
class exampleclass:
    eyes="blue"
    age=22
    def thismethod(self):
        return 'hey the method worked'

class classname():
    def createName(self,name):
        self.name=name
    def displayName(self):
        return(self.name)
    def saying(self):
        print("Hello %s" % self.name)

first=classname()
second=classname()

first.createName("Betsy")
second.createName("CAT")
'''
print(first.displayName())
'''
print(second.displayName())


exampleObject=exampleclass()
print (exampleObject.eyes)
if exampleObject.age < 23:
    print (exampleObject.thismethod())