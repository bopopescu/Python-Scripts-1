def main ():
    numberlist = [1,2,3,4,5]
    for x in numberlist:
        print(x, end="\t")
    print("\n")
    for x in range(1,100):
        if x > 50:
            continue
        print(x)

if __name__ == '__main__':
    main()