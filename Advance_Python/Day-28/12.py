# const over

class Parent():
    def __init__(self,id,name):
        print('Parent Const...')
        self.id = id
        self.name = name

    def m1(self):
        print('Parent Method')
        print('PName is : ',self.name)
        print('PID is : ',self.id)


class Child(Parent):
    def __init__(self,id,name):
        print('Child Const...')
        self.id = id
        self.name = name

    def m1(self):
        print('Child Method')
        print('CName is : ',self.name)
        print('CID is : ',self.id)

Child(101,'Micky').m1()




