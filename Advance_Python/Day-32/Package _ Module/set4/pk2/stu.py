# 
class Student():
    def __init__(self,sid,sname,scity,sbook):
        self.sid = sid
        self.sname = sname
        self.scity = scity
        self.sbook = sbook

    def Stu_status(self):
        print('Student ID = {}   Student Name = {} '.format(self.sid,self.sname))

    def stu_code(self):
        print('Student City = {}   Student Book = {} '.format(self.scity,self.sbook))

    










