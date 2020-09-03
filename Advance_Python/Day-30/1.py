# Encapsulation

# without

class Myclass():
    # class variable
    a = 10

    # method
    def m1(self):
        print('A is not a private variable and its value is : ',self.a)

c = Myclass()
c.m1()

print('Value of class variable is : ',c.a)


