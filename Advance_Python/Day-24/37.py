# cont and class and method

class Employee():
    # class Variable
    a = 10
    b = 20

    # cont
    def __init__(self,c,d):
        print('Const - ',(c+d))

    def m1(self):
        print('Method - 1 : ',(self.a+self.b))

ee =  Employee(30,40)
ee.m1()


