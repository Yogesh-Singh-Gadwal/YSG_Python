# Encapsulation

class Myclass():
    print('Parent Class')
    # class variable
    a = 10
    b = 20
    print(a)
    print(b)
    
print()

class Child(Myclass):
    print('Child Class')
    print(Myclass.a)
    print(Myclass.b)

