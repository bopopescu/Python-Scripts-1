
def countway(n):
    count = [0,1,2,4]
    if n < 4:
        return(count[n])
    else:
        ways=0
        start = 3
        while n > start:
            ways = ways + count[3] + count[2] + count[1]
            count.append(ways)
            start +=1
    print(count)
    return(count[n])

p=int(input("# of Steps"))
print(countway(p))