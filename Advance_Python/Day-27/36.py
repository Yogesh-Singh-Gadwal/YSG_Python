# inheritance 

class Parent1():
    pass

class Parent2():
    def m1(self):
        print('Parent-2')

class Child2(Parent1,Parent2):
    def m1(self):
        print('Child')
    
    def m2(self):
        super().m1()
        self.m1()

cc = Child2()
cc.m2()


