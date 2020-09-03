# inheritance

class Parent(object):
    def __init__(self,eid,ename):
        self.eid = eid
        self.ename = ename 


class Child(Parent):

    def m1(self):
        print('Student ID : ',self.eid)
        print('Student Name : ',self.ename)    

cc = Child(101,'Micky')
cc.m1()





