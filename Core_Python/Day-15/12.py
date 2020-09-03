# Function 
# lamda funx

# normal funx
l1  = [1,2,3,4,5,6,7,8,9]
l2 = []
def myfun(l1):
    for x in l1:
        if x%2 == 0:
           l2.append(x)
        else:
            pass    

myfun(l1)
print('Value is : ',l2)


# filter

l2  = [1,2,3,4,5,6,7,8,9]
def m2(x):
    if x%2 == 0:
        return True
    else:
        return False


print('Result is : ',list(filter(m2,l2)))



# lambda  + filter

l3  = [1,2,3,4,5,6,7,8,9]

print('Final Result is : ',list(filter(lambda x : x%2 == 0,l3)))



