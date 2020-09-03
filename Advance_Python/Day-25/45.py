# Const
from time import sleep
class Employee():
    # 1 st
    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def __str__(self):
        return 'Welcome : %s '%(self.ename) 

    def employeeStatus(self):
        print('Employee Id : ',self.eid)
        print('Employee Name : ',self.ename)
        print('Employee Salary : ',self.esal)
        print();print()
        
ee = Employee(101,'Micky',9000000)
print(ee)
sleep(3)
print()
print('Your Status Record is : ')
ee.employeeStatus()

print()
sleep(4)

ee = Employee(102,'Ajay',450000)
print(ee)
sleep(3)
print()
ee.employeeStatus()


