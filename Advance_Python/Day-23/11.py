# Class and Objects

class Employee():
    # class variables
    a = 10
    b = 20
    # method
    def m1(self):
        # local variables
        c = 30
        d = 40
        print('Sum of value is : ',(self.a+self.b))
        print('Value of C is : ',c)
        print('Value of D is : ',d)
    
    
ee = Employee()
ee.m1()
