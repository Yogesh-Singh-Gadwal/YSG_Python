# Class & Object
class Employee():
    
    # method
    def m1(self,a,b):
        self.a = a+5
        self.b = b+5
        print('Sum of the value : ',a+b)
        print('Mul of value is : ',(self.a*self.b))
        print()

    def m2(self):
        print('Method-2 Value-1 is ',self.a)
        print('Method-2 Value-2 is ',self.b)
        
e1 = Employee()
e1.m1(5,7)
e1.m2()
print();print()

e2 = Employee()
e2.m1(50,70)
e2.m2()


       