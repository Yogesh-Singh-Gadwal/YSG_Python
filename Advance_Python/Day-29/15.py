# Abstraction

from abc import ABC,abstractmethod

class Employee(ABC):
    # const
    def __init__(self,name):
        self.name = name
  
class Child1(Employee):
    # override    
    def m1(self):
        name = self.name
        print('Micky ...... -1  ',self.name)

class Child2(Child1):    
    # override
    def m1(self):
        self.name = 'Akira'
        print('Micky ...... -2  ',self.name)

class Child3(Child2):
    pass

cc = Child3('Disney')
cc.m1()


