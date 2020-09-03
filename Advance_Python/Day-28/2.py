# polymorphism

class Parent():
    ename = 'disney'

class Child(Parent):
    sname = 'Micky'


cc = Child()
print('Value is : ',cc.ename)
print('Value is : ',cc.sname)
