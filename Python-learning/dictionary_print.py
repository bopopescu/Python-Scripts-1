

my_set={1,2,3,4,5,6,7}
my_tuple=(7,6,5,4,3,2,1)

my_dict={"1":"timepass1", "2":"timepass2", "4":"timepass4", "3":"timepass3"}

for i in my_set:
    print(i)

print(my_set)

for j in my_tuple:
    print(j)

print (my_tuple)

for key,val in my_dict.items():
    print( "My dictionary %s whose value is %s" %(key,val))

print (my_dict)
print(sorted(my_dict.keys()))

print (sorted(my_dict.values()))