# polymorphism

# no variable overridding


class Parent():
    ename = 'Micky'

class Child(Parent):
    pass


cc = Child()
print('Value is : ',cc.ename)



