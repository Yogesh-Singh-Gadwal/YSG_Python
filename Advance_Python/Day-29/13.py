# Abstraction

from abc import ABC,abstractmethod

class Employee(ABC):
    # const
    def __init__(self,name):
        self.name = name

    # abstract method
    @abstractmethod
    def m1(self):
        pass
    
class Child1(Employee):
    # override
    def m1(self):
        print('Micky ...... -1  ',self.name)


class Child2(Employee):
    # override
    def m1(self):
        print('Micky ...... -2  ',self.name)



cc = Child1('Disney')
cc.m1()
print()
cc = Child2('India')
cc.m1()
