class no(object):
    def __init__(self, number):
        self.number=number

    def square(self):
        return self.number**2


if __name__ == '__main__':
    p=int(input("Finding square of number? --->"))
    n = no(p)
    print(n.square())