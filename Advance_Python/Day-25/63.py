# class object
import time
class Employee():
    # const
    def __del__(self):
        print('Object is deleted...')
    # method
    def cal(self,a,b):
        print('Sum of value is : ',a+b)


e1 = Employee()
e2 = Employee()
e3 = Employee()

e1.cal(2,3)
print()
time.sleep(2)

e2.cal(4,5)
print()
time.sleep(2)


e3.cal(6,7)
print()

time.sleep(2)
