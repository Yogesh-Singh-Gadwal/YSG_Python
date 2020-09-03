# inheritance

class Parent(object):
    def __init__(self,eid,ename):
        self.eid = eid
        self.ename = ename 

class Child(Parent):
    def __init__(self,eid,ename):   
        print('Child Const -1')
        print('Employee Id : ',eid)
        print('Employee Name : ',ename)

    def m1(self):
        print('Student ID : ',self.eid)     # AttributeError: 'Child' object has no attribute 'eid'
        print('Student Name : ',self.ename)    

cc = Child(101,'Micky')
cc.m1()





