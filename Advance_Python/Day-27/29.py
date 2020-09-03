#   inheritance

class Parent1():
    pass

class Parent2():
    def m1(self):
        print('Parent -2 ')

class Child(Parent1,Parent2):
    pass


cc =  Child()
cc.m1()


