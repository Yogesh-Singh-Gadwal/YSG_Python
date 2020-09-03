# functions
# variable 

# global variable
ename = 'micky'

def m1():  
    # local variable
    ename = 'akira'       
    print('Value is : ',ename)
    print('Value is : ',globals()['ename'])   

m1()

# global memory
print('Value is : ',ename)

