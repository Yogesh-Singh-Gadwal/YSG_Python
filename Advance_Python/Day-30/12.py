# Encapsulation

class Myclass():
    # method(Private)
    def m1(self):
        print('Parent Method - 1')

    def __m2(self):
        print('Parent Method - 2')

class Child(Myclass):
    pass

cc = Child()
cc.m1()
cc.__m2()  # AttributeError: 'Child' object has no attribute '__m2'


