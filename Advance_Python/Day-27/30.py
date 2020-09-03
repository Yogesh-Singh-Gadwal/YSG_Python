#   inheritance

class Parent1():
    def m1(self):
        print('Parent -1 ')

class Parent2():
    def m1(self):
        print('Parent -2 ')

class Child(Parent1,Parent2):
    def m1(self):
        print('Child-1 ')


cc =  Child()
cc.m1()


