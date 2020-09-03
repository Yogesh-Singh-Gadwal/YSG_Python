# Const
# class
class Myclass():
    def __init__(self):
        print('Const -1')

    def m1(self,a,b):
        self.a = a
        self.b = b
        print('Method-1')


    def all_Sum(self):
        print('Sum of value is : ',(self.a+self.b))

ee = Myclass()
v1 = int(input('Enter user value-1 : '))
v2 = int(input('Enter user value-2 : '))

ee.all_Sum()    # AttributeError: 'Myclass' object has no attribute 'a'
ee.m1(v1,v2)



