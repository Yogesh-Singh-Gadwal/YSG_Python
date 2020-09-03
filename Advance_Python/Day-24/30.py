# Const
# class
class Myclass():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print('Const -1')

    def all_Sum(self):
        print('Sum of value is : ',(self.a+self.b))

    def mul(self):
        print('Result of Mul value is : ',(self.a*self.b))

v1 = int(input('Enter user value-1 : '))
v2 = int(input('Enter user value-2 : '))

ee = Myclass(v1,v2)

print()
ee.all_Sum()

print()
ee.mul()
  



