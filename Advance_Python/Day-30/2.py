# Encapsulation

# without

class Myclass():
    # class variable
    __a = 10

    # method
    def m1(self):
        print('A value is : ',self.__a)

c = Myclass()
c.m1()
print()
print('Value of class variable is : ',c.__a)  # AttributeError: 'Myclass' object has no attribute '__a'


