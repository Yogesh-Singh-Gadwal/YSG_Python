# inheritance

class Parent(object):
    def m1(self):
        print('Parent Class Method')


class Child(Parent):
    def m1(self):
        print('Child Class Method')    

    def m2(self):
        super().m1()    

cc = Child()
cc.m1()
cc.m2()


