# Exception Handling
# Abnormal termination
try:
    print('Micky-1')
    print('Micky-2')
    print('Micky'+10)    # TypeError: can only concatenate str (not "int") to str
except ZeroDivisionError as z:
    print('Exception raised due to : ',z)    
print()
print('Rest of the code...')

