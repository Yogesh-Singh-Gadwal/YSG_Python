# function
# variable arguments

def m1(*args):
    y = 0
    for x in args:
        y = x+y
    print('Sum of value is : ',y)    


m1(10)
m1(10,20)
m1(10,20,30)
m1(10,20,30,40)
m1(10,20,30,40,50)
m1(10,20,30,40,50,60)

