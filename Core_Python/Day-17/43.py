# multiple values 

try:
    a,b = eval(input('Value-1 and Value -2 : '))
    print(a/b)
except ArithmeticError as ae:
    print('Arithmetic Exception due to : ',ae)
except Exception as e:
    print('Exception due to : ',e)  



