# method over

class Parent():
    def m1(self,a,b):
        print('Parent Method....')

class Child(Parent):
    def m1(self):   
        print('Child Method....')


cc = Child()
cc.m1(20,30) # TypeError: m1() takes 1 positional argument but 3 were given


