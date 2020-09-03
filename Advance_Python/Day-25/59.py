# class and object

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
        print('Deposite Amount is : ',self.bal)
    
    def withdraw(self,amount):
        if amount > self.bal:
            raise RuntimeError("Withdraw amount is greater than deposite amount ")
        else:
            self.bal = self.bal-amount   


print('Welcome python Bank : ')
v1 = input('would you like to open an account : ').lower()
l1 = ['yes','y']
print()
if v1 in l1:
    name = input('Enter user name for Account : ')
    bal = float(input('Enter min bal to open account : '))
    cc = Customer(name,bal)
    print()
    print('Cong your Account is open in Python Bank')
    print('User name : ',cc.name)
    print('ACcount bal is : ',cc.bal)
    print()
     
    v2  = input('Would like to deposite Amount in your Account : ')
    if v2 in l1:
        print()
        deposite_amount = float(input('Enter Your Amount to Deposite : '))
        cc.deposite(deposite_amount)
        print()
        v2  = input('Would like to withdraw Amount from your Account : ')
        if v2 in l1:
            print()
            withdraw_amount = float(input('Enter withdaw amount value : '))
            cc.withdraw(withdraw_amount)
            print()
            v2  = input('Would like to Total Account Balance : ')
            if v2 in l1:
                print()
                print('Total Balance is : ',cc.bal)

        else:
            print('Thank you for your Visit')    
    else:
        print('Good Day') 
else:
    print('Thank you .. Have a good day')        



