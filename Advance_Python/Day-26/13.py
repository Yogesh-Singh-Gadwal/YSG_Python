# inheritance

class Parent(object):
    def m1(self):
        print('Parent Method-1 ')

class Child(Parent):
    pass

c = Child()
c.m1()
print()
print(dir(Child))

