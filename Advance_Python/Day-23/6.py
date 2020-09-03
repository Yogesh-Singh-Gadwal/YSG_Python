# Class and Objects

class Employee():
    # class variables
    a = 10
    b = 20
    # method
    def m1(self):
        print('Value of A is : ',self.a)
        print()
        print('Value of B is : ',self.b)

ee = Employee()
ee.m1()
print()
print('Value is : ',ee.a)
