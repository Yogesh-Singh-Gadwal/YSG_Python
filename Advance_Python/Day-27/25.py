# multiple inheritance

class Parent():
    def m1(self):
        print('Parent')

class Child1(Parent):
    def m2(self):
        print('Child-1')

class Child2(Child1):
    def m3(self):
        print('Child-2')

cc = Child2()
cc.m1()
cc.m2()
cc.m3()

