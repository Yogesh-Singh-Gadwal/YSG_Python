# Class & Object

class Employee():
    a = 10
    b = 20
    # method
    def m1(self):
        print('Sum of value is : ',(self.a+self.b))
    
    def m2(self):
        print('Mul of values is : ',(self.a*self.b))

# 1st way
ee = Employee()
ee.m1()
ee.m2()
print('Class Variable : ',ee.a)
print('Class Variable : ',ee.b)


