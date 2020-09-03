# Encapsulation

class Myclass():
    # class variable
    __a = 50
    # sett method
    def setA(self,v1):
        self.__a = v1
    # gett method
    def getA(self):
        return self.__a

mm = Myclass()
v1 = float(input('Enter user value : '))
mm.setA(v1)

print()

print('Value of private variable is : ',mm.getA())

      