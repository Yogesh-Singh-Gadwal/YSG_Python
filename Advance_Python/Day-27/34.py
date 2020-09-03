# inheritance 

class Parent():
    def m1(self):
        print('Parent')

class Child1(Parent):
    pass

class Child2(Child1):
    def m1(self):
        print('Child')
    
    def m2(self):
        super().m1()
        self.m1()

cc = Child2()
cc.m2()

