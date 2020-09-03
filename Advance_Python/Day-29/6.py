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

Employee()   # TypeError: Can't instantiate abstract class Employee with abstract methods m1


