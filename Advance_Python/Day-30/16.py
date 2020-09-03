# Encapsulation

class Myclass():
    # class variable
    __a = 50
    __b = 0
    # sett method
    def m1(self,v1):
        self.__a = v1
    # method
    def m2(self):
        print('Value is  : ',self.__a)
        print('Value is  : ',self.__b)

mm = Myclass()
v1 = float(input('Enter user value : '))
mm.m1(v1)
mm.m2()
print()

      