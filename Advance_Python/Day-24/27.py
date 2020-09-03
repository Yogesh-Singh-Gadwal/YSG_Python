# Class and object

class Myclass():
    def m1(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        print('Sum of the value is : ',(self.a+self.b))

    def mul(self):
        print('Mul of value is : ',(self.a*self.b))


m = Myclass()
v1 = int(input('Enter user value-1 : '))
v2 = int(input('Enter user value-2 : '))
m.m1(v1,v2)
print()
m.add()
print()
m.mul()



