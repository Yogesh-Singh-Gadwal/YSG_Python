# Function 
# lamda funx

# normal funx
def myfun(x,y):
    if x > y:
        return x
    else:
        return y    

v1 = myfun(10,20)    
print('Value is : ',v1)

# lambda

v1 = lambda x,y : x if x > y else y
print('Result is : ',v1(67,123))

