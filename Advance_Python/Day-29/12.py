# Abstraction

from abc import ABC,abstractmethod

class Employee(ABC):
      
    # abstract method
      @abstractmethod
      def m1(self):
          pass

    # abstract method
      @abstractmethod
      def m2(self):
          pass


class Child1(Employee):
    # override
    def m1(self):
        print('Micky ...... -1  ')


class Child2(Child1):
    # override
    def m2(self):
        print('Micky ...... -2  ')

cc = Child2()
cc.m1()
cc.m2()

