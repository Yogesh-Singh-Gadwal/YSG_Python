# method over

class Parent():
    def m1(self):
        print('Parent Method....')

class Child(Parent):
    def m1(self):
        print('Child Method....')


cc = Child()
cc.m1()
