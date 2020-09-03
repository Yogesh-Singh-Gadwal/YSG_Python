# Class & Object

class Employee():
    
    # method
    def m1(self,a,b):
        print('Sum of value is :',a+b)

    def m2(self):
        print('Product value is : ',(a*b))  # NameError: name 'a' is not defined


ee = Employee()
v1 = float(input('Enter user value -1 : '))
v2 = float(input('Enter user value -2 : '))
ee.m1(v1,v2)
ee.m2()



