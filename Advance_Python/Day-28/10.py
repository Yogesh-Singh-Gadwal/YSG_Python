# const over

class Parent():
    def __init__(self):
        print('Parent Const...')

class Child(Parent):
    def __init__(self):
        print('Child Const...')

Child()


