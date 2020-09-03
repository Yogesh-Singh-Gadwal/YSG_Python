# Has attr
# To check the attribute present in class or not

class Employee:
    # const 
    def __init__(self,eid,ename):
        self.eid = eid
        self.ename = ename 

emp1 = Employee(101,'Micky')

emp2 = Employee(102,'Rahul')

print(hasattr(emp1,'eid'))

print(hasattr(emp2,'ename'))

print(hasattr(emp2,'eadd'))


