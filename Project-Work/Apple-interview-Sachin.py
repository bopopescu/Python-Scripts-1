
def main():
    s=[]
    i=0
    p=[]
    f=open("student.txt", 'r')
    for lines in f:
        s.append(lines.split('^^^^'))
        i = i + 1

# Create set of unique class
    for j in range(i):
        p.append(int(s[j][1]))
    u=set(p)

# sort the list based on the 3rd element
    for j in range(i):
        for k in range(j,i):
            if int(s[k][2]) > int(s[j][2]):
                temp=s[k]
                s[k]=s[j]
                s[j]=temp
# Print the sorted list for each class
    for cl in u:
        print("For class %s" %(cl))
        for x in range(i):
            if int(s[x][1]) == cl:
                print("%s got %s" % (s[x][0], s[x][2]))

if __name__ == '__main__':
    main()