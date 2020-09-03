# Class and Object
from time import sleep
class Employee:
    #class variable
    empcount = 0
    # const
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount +=1 

    def __str__(self):
        return "Name :{0}  Salary : {1}".format(self.name,self.salary)
    
    def displaycount(self):
        print('Total Employee Count is : %d'%Employee.empcount)
        print()
        print('Total Employee Count is : ',Employee.empcount)
 
ee = Employee('A',900000)
print(ee)
print()
sleep(3)
ee = Employee('B',600000)
print(ee)
print()
sleep(3)
ee = Employee('C',300000)
print(ee)
print()
sleep(3)
ee = Employee('D',200000)
print(ee)
sleep(3)

print()
ee.displaycount()


