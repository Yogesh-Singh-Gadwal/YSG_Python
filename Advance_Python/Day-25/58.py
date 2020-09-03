# class and object
from time import sleep
class Customer:
    # const
    def __init__(self,name,bal=0.0):
        self.name = name
        self.bal = bal
    
    def __str__(self):
        return self.name+' -- '+str(self.bal)

    def __del__(self):
        print('You have Succsessfuly Log-Out Now')    

    # method
    def deposite(self,amount):
        self.bal = self.bal+amount
        print('Total Deposite Amount is : ',self.bal)
    
    def withdraw(self,amount):
        if amount > self.bal:
            raise RuntimeError("Withdraw amount is greater than deposite amount ")
        else:
            self.bal = self.bal-amount   

        
name = input('Enter user name : ')
bal = float(input('Enter min bal to open account : '))
print()
cc = Customer(name,bal)
print('Account is created with status : ',cc)
sleep(3)
print()

deposite_amount = float(input('Enter user Amount : '))
cc.deposite(deposite_amount)
sleep(3)
print()

withdraw_amount = float(input('Enter withdaw amount value : '))
cc.withdraw(withdraw_amount)
sleep(3)
print()

print('Total Balance is : ',cc.bal)
sleep(2)
print()





