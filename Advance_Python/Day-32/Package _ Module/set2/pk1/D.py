def withdraw(amount):
    bal = 7000
    if bal > amount:
        bal = bal - amount
        print('Total Amount remaining is : ',bal)
    else:
        print('withdraw amount is not sufficent ...... ')