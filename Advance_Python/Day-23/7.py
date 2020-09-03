# Class and Objects

class Employee():
    # class variables
    a = 10
    b = 30
    # method
    def m1(self):
        print('Value of A is : ',self.a)
        print()
        print('Value of B is : ',self.b)
        print()

    # method
    def m2(self):
        print('Sum of Value is : ',self.a+self.b)
        print()
       

ee = Employee()
ee.m1()
ee.m2()

