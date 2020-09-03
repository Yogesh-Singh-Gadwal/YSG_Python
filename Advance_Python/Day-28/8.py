# method over

class Parent():
    def m1(self,c,d):
        print('Discount - 50%')

class Child(Parent):
    def m1(self,a,b):   
        print('Discount - 70%')
    

cc = Child()
cc.m1(20,30) 



