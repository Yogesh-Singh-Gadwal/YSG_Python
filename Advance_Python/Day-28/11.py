# const over

class Parent():
    def __init__(self,id,name):
        print('Parent Const...')
        self.id = id
        self.name = name

    def m1(self):
        print('Parent Method')
        print('Name is : ',self.name)
        print('ID is : ',self.id)


class Child(Parent):
    pass

Child(101,'Micky').m1()




