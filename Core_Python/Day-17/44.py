# multiple values 

try:
    print(eval(input('Value-1 and Value -2 : ')))    
except ArithmeticError as ae:
    print('Exception due to : ',ae)
except Exception as e:
    print('Exception due to : ',e)  


