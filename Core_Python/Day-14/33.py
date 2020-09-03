# variable

# local variables
# scope
def m1():
    # local variables
    a = 10
    print('Value is : ',a)

m1()

def m2():    
    print('Value is : ',a)  # NameError: name 'a' is not defined

m2()
