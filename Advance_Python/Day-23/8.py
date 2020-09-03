# Class and Objects

class Employee():
    # class variables
    a = 10
    b = 20
    # method
    def m1(self,c,d):
        print('Value of A is : ',self.a)
        print('Value of C is : ',c)
        print()
        print('Value of B is : ',self.b)
        print('Value of D is : ',d)
        print()

    # method
    def m2(self,e,f):
        print('Sum of Value is : ',self.a+self.b+e+f)
        print()
       

ee = Employee()
ee.m1(3,4)
ee.m2(5,6)

