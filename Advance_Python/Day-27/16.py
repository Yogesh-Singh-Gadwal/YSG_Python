# inheritance

class Parent(object):
    def __init__(self,eid,ename):
        print('Parent Const -1')
        print('Employee Id : ',eid)
        print('Employee Name : ',ename)

class Child(Parent):
    def __init__(self,eid,ename):
        print('Child Const -1')
        print('Employee Id : ',eid)
        print('Employee Name : ',ename)

Child(101,'Micky')




