# Class and Objects

# Global Variables
e = 50
f = 60
class Employee():
    # class variables
    a = 10
    b = 10
    # method
    def m1(self):
        # local variables
        c = 30
        d = 40
        print('Sum of value is : ',(self.a+self.b))
        print('Local Variable Value of C is : ',c)
        print('Local Variable  Value of D is : ',d)
        print('Global Variable Value of E is : ',e)
        print('Global Variable Value of F is : ',f)
    
    
ee = Employee()
ee.m1()
