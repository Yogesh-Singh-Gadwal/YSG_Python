# Exception Handling

try:
    v1 = int(input('Enter user value : '))
    print(10/v1)
    print(b)
except TabError as tb:
    print(tb)
except NameError as ne:
    print('Result is : ',ne)
except ValueError as ve:
    print('Value : ',ve)
except ImportError as ie:
    print(ie)
except:
    print('i dont know')  

