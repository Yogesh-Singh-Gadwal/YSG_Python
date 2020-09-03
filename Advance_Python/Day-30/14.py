# Encapsulation

class Myclass():
    # class variable
    __a = 50
    # const
    def __init__(self,v1):
        self.__a = v1
    # method
    def m1(self):
        print('Value is  : ',self.__a)

mm = Myclass(80)

print()
print(mm.__a) # AttributeError: 'Myclass' object has no attribute '__a'


      