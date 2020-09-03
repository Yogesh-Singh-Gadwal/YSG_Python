# Class & Object

# Instance and Static

class Employee():

    # instance 
    def m1(self,city,phone):
        print('Instance method -1','  : ',city,' -> ',phone)

    # static
    @staticmethod 
    def m2(name,email):
        print('Static method -1','  : ',name,'  ->  ',email)

# Static
Employee.m2('Micky','m@gmail.com')      

# Instance
Employee().m1('Hyd',99887766)



