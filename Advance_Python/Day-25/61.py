# Has attr
# To check the attribute present in class or not
import time
class Employee:
    # const 
    def __init__(self,eid,ename):
        self.eid = eid
        self.ename = ename 

emp1 = Employee(101,'Micky')
print(hasattr(emp1,'phone'))
time.sleep(3)
print()

setattr(emp1,'phone',99887766)
print(hasattr(emp1,'phone'))
print()

time.sleep(3)

print(getattr(emp1,'phone'))

delattr(emp1,'phone')
print()
time.sleep(3)
print(hasattr(emp1,'phone'))












