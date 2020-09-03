# Const
# class

# global variables
a = 100
b = 200
class Employee():
    # class variables
    a = 10
    b = 20
    # const
    def __init__(self,a,b):
        print('Local variable : ',a)
        print('Local variable : ',b)
        print('Class variable : ',self.a)
        print('Class variable : ',self.b)
        print('Global variable : ',globals()['a'])
        print('Global variable : ',globals()['b'])

Employee(30,40)



