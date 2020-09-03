# Abstraction

from abc import ABC,abstractmethod

class Employee(ABC):
      
    # abstract method
      @abstractmethod
      def m1(self):
          pass
        
    # instance method
      def m2(self):
          print('Employee class data-1...')
    # instance method
      def m3(self):
          print('Employee class data-2...')
    # instance method
      def m4(self):
          print('Employee class data-3...')        

class Child(Employee):
    # overridding
    def m1(self):
        print('Micky...')


c = Child()
c.m1()
c.m2()
c.m3()
c.m4()





