# Abstraction

from abc import ABC,abstractmethod

class Employee(ABC):
      
      # abstract method
      @abstractmethod
      def m1(self):
          pass
      # instance method
      def m2(self):
          print('Employee class data...')

class EmpStatus(Employee):
    # overridding
    def m1(self):
        print('Micky......')

ee = EmpStatus()
ee.m1()
ee.m2()





