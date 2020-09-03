# Hierarchical inheritance

class Parent():
    def m1(self):
        print('Parent')

class Mahesh(Parent):
    def m2(self):
        print('Mahesh')

class Rahul(Parent):
    def m2(self):
        print('Rahul')


mm = Mahesh()
mm.m1()
mm.m2()

print()

rr = Rahul()
rr.m1()
rr.m2()

