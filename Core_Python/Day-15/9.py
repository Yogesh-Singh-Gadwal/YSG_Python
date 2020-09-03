# Function 
# lamda funx

# normal funx
def myfun(x):
    return x+2

v1 = myfun(10)    
print('Value is : ',v1)
# or 
print('Value is : ',myfun(10))

print()
# lambda

v1 = lambda x : x+2

v2 = v1(20)
print('Result is : ',v2)
# or
print('Result is : ',v1(20))
