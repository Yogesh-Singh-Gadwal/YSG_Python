# list 
# extend()

l1 = ['a','b','c']
l2 = ['d','e','f']
l3 = ['g','h','i','j']
l4 = []
l5 = [l1,l2,l3]
for x in l5:
    l4.extend(x)


print('Result is : ',l4)
