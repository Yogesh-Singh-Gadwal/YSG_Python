# Encapsulation

class Myclass():
    print('Parent Class')
    # class variable
    __a = 10
    b = 20
    print(__a)
    print(b)
    
print()

class Child(Myclass):
    print('Child Class')
    print(Myclass.__a)  # AttributeError: type object 'Myclass' has no attribute '_Child__a'
    print(Myclass.b)


