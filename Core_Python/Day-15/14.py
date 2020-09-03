# map 

l1 = [2,3,4,5]
def m1(x):
    return x *2

print('Value is : ',list(map(m1,l1)))


# lambda + map

l2 = [2,3,4,5]

print('Result is : ',list(map(lambda x : x*2,l2)))

