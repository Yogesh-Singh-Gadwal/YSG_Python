# Abstraction

from abc import ABC,abstractmethod

class Employee(ABC):
      
      # abstract method
      @abstractmethod
      def m1(self):
          pass

class EmpStatus(Employee):
    # overridding
    def m1(self):
        print('Micky......')

ee = EmpStatus()
ee.m1()




