# inheritance

class Parent(object):
    def __init__(self,eid,ename):
        print('Parent class ')
        self.eid = eid
        self.ename = ename 


class Child(Parent):
    def __init__(self,eid,ename):
        print('Child class ')
        self.eid = eid
        self.ename = ename 

    def m1(self):
        print('Student ID : ',self.eid)
        print('Student Name : ',self.ename)    

cc = Child(101,'Micky')
cc.m1()





