# 
class Employee():
    def __init__(self,eid,ename,ecity,esalary):
        self.eid = eid
        self.ename = ename
        self.ecity = ecity
        self.esal = esalary

    def emp_status(self):
        print('Employee ID = {}   Employee Name = {} '.format(self.eid,self.ename))

    def emp_code(self):
        print('Employee City = {}   Employee Salary = {} '.format(self.ecity,self.esal))