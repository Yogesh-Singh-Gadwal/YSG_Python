# inheritance

class Parent(object):
    v1,v2 = 100,200


class Child(Parent):
    def m1(self):
        print('Child Class Method')   
        print('Result is : ',self.v1+self.v2)


cc = Child()
cc.m1()



