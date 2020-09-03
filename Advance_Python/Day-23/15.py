# Class & Object

class Employee():
    a = 10
    b = 20
    # method
    def m1(self):
        print('Sum of value is : ',(self.a+self.b))

# 1st way
ee = Employee()
ee.m1()


# 2nd way

Employee().m1()

