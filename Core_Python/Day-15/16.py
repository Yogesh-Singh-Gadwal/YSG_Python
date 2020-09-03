# reduce 

from functools import reduce

l1  = [1,2,3,4,5,6,7,8,9]

cu = 0
def m1(l1):
    global cu
    for x in l1:
        cu = cu+x
m1(l1)
print('Value is : ',cu)

# reduce with lambda

l2  = [1,2,3,4,5,6,7,8,9] 
print('Result is : ',reduce(lambda x,y : x+y,l2))


