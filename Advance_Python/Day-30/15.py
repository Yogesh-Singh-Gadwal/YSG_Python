# Encapsulation

class Myclass():
    # class variable
    __a = 50
    __b = 0
    # const
    def __init__(self,v1,v2):
        self.__a = v1
        self.__b = v2
    # method
    def m1(self):
        print('Value is  : ',self.__a)
        print('Value is  : ',self.__b)

mm = Myclass(80,120)
mm.m1()
print()

      