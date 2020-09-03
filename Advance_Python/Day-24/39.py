# cont and class and method

class Employee():  
    # cont
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def m1(self):
        print(self.a+self.b)

    def m2(self):
        print(self.a*self.b)
        
ee = Employee(5,7)
ee.m1()
ee.m2()
print(ee.a)
print(ee.b)

