# Const
class Employee():
    # 1 st
    def __init__(self,ename):
        self.ename = ename
       
    def __str__(self):
        return self.ename

    def employeeStatus(self):        
        print('Employee Name : ',self.ename)        
        print();print()
        


ee = Employee('Micky')
print(ee)
if ee != ' ':
    ee.employeeStatus()
else:
    print('Value is not present')    
print()




