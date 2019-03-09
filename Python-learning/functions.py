x=5

def website (font='TNR', backgroundcolor= 'Black', size='10', color='blue'):
    print ("Font is", font)
    print ("Background color is", backgroundcolor)
    print ("Size is", size)
    print("Front color", color)

def example():
    z = 15
    y = x + 1
    print('Value of Y in example', y)
    print('Value of X in example', x)
    return y

def main():

    website('Arial','black')
    x = example()
    print(x)

if __name__ == '__main__':
    main()
