# inheritance

class Parent(object):
    def m1(self):
        print('Parent Method-1 ')

class Child(Parent):
    def m2(self):
        print('Child Method-1')

c = Child()
c.m2()
c.m1()
print()
print(dir(Child))

