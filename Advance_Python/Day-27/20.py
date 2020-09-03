# inheritance

class Parent(object):
    def m1(self):
        print('Parent Class Method')


class Child(Parent):
    def m1(self):
        print('Child Class Method')    

cc = Child()
cc.m1()
#Parent().m1()





