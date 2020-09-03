# Class and Objects

# Global Variables
a = 500
b = 600
class Employee():
    # class variables
    a = 10
    b = 20
    # method
    def m1(self):
        # local variables
        a = 300
        b = 400
        print('Local Variable : ',a)
        print('Local Variable : ',b)
        print('Class Variable : ',self.a)
        print('Class Variable : ',self.b)
        print('Global Variable : ',globals()['a'])
        print('Global Variable : ',globals()['b'])
    
ee = Employee()
ee.m1()

