# inheritance

class Parent(object):
    pass

class Child(Parent):
    def m2(self):
        print('Child Method-1')

c = Child()
c.m2()

print(dir(Child))

