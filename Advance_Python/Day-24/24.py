# Class & Object

# Instance and Static

class Employee():

    # instance 
    def m1(self):
        print('Instance method -1')

    # static
    @staticmethod 
    def m2():
        print('Static method -1')

Employee.m2()      
Employee().m1()

