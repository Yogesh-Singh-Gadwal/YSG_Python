# inheritance 
# hybrid

class Parent():
    def m1(self):
        print('Parent...')

class Akira(Parent):
    def m2(self):
        print('Akira')

class Micky(Parent):
    def m2(self):
        print('Micky')

class Python(Micky,Akira):
    def m3(self):
        print('Python')

p = Python()
p.m1()
p.m2()
p.m3()



