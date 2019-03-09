class student(object):
    rise = 0.5
    emailsuffix="vmware.com"

    def __init__(self, name, salary, marks):
        self.name=name
        self.salary=salary
        self.marks=marks
        self.email=self.name+self.emailsuffix


    def __str__(self):
        return "Student " + self.name

    def fullname(self):
        fn=self.name+"Nagwekar"
        return '{} {}'.format(self.name,"Nagwekar")

    def appraise(self):
        self.marks= int (self.marks * self.rise)
        return self.marks

x = student("Parag", 1000, 40)
y = student("Roopam", 1000, 50)

print(x)

print (x.fullname())

print (x.name)
print (x.salary)
print (x.marks)
x.appraise()
print (x.marks)
print(x.appraise())

print (y.name)
print (y.salary)
print (y.marks)
print (y.appraise())

class dumb(student):
        rise=1.5
        emailsuffix="@yahoo.com"

std_1=student("Beel", 200, 40)
print (std_1.email)
print(std_1.marks)


