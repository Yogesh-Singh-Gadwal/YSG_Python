# Const
# class

# global variables
c = 100
d = 200
class Employee():
    # class variables
    a = 10
    b = 20
    # const
    def __init__(self,a,b):
        print(a)
        print(b)
        print(self.a)
        print(self.b)
        print(c)
        print(d)

Employee(30,40)