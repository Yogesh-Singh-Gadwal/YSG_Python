# Class and Object
from time import sleep

class Employee():
    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
    
    def employeeStatus(self):
        print('Employee Id : ',self.eid)
        print('Employee Name : ',self.ename)
        print('Employee Salary : ',self.esal)
        print();print()

# 1st
e1 = Employee(101,'Micky',900000)        
e1.employeeStatus()
sleep(3)
# 2nd way
Employee(102,'Rahul',35000).employeeStatus()


