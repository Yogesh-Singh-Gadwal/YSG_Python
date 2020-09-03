# class 
from time import sleep
# global variable
c = 30
import time
class Myclass():
    # class variable
    a = 10
    # cons-1
    def __init__(self,name):
        self.name = name

    # cons-2
    def __str__(self):
        return self.name 

    # cons-3
    def __del__(self):
        print('Object is deleted...')
        
    # method
    def m1(self):
        b = 20
        print('Sum of value is : ',self.a+b+c)

c1 = Myclass('Micky')
print('Name is : ',c1)
sleep(2)

c1.m1()
print('Class Variable:',c1.a)
sleep(2)

del c1




