# method over

class Parent():
    def m1(self,c,d):
        print('Parent Method....')

class Child(Parent):
    def m1(self,a,b):   
        print('Child Method....')


cc = Child()
cc.m1(20,30) 


