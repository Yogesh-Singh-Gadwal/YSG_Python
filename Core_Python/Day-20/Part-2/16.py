# tuple 

t1 = ('a','b','c')
print(type(t1))
print('Value is : ',t1)

# converstion

l1 = list(t1)
l1[1] = 'Z'

# converstion

t1 = tuple(l1)
print(type(t1))
print('Value is : ',t1)


