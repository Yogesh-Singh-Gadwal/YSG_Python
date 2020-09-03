# Abstraction

from abc import ABC,abstractmethod

class Employee(ABC):
      
    # abstract method
      @abstractmethod
      def m1(self):
          pass

class Child(Employee):
    pass

Child()  # TypeError: Can't instantiate abstract class Child with abstract methods m1



