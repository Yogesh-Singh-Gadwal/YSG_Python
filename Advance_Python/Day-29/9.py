# Abstraction

from abc import ABC,abstractmethod

class Employee(ABC):
      
    # abstract method
      @abstractmethod
      def m1(self):
          pass

class Child1(Employee):
    def m1(self):
        print('Child -1 data ')

class Child2(Employee):
    def m1(self):
        print('Child -2 data ')

c1 = Child1()
c1.m1()
print()

c2 = Child2()
c2.m1()
print()

