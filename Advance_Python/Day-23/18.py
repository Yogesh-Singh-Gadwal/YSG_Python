# Class & Object

class Employee():
    a = 10
    b = 20
    # method
    def bank_Status(self,balance=500,amount=7000):
        print('Total Amount is : ',(balance+amount))


# 1st Object
mahesh = Employee()
print('Object -1 Id : ',id(mahesh))
print('Bank Status For Mahesh is : ', end ='')
mahesh.bank_Status()
print()



# 2nd Object
rahul = Employee()
print('Object -2 Id : ',id(rahul))
print('Bank Status For Rahul is : ', end ='')
rahul.bank_Status(10000)
print()


# 3rd Object
harsha = Employee()
print('Object -3 Id : ',id(harsha))
print('Bank Status For Harsha is : ', end ='')
harsha.bank_Status(30000,12000)
print()


