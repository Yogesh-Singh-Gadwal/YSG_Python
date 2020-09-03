# inheritance 

class Parent():
    def m1(self):
        print('Parent')

class Child(Parent):
    def m1(self):
        print('Child')
    
    def m2(self):
        super().m1()
        self.m1()

cc = Child()
cc.m2()





