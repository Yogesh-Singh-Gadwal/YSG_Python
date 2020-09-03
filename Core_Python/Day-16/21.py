# Exception
try:
    a = int(input('Enter user value : '))
    print(10/a)
    print('Micky'+a)
except(MemoryError) as tz:    
    print('Exception due to :',tz)
except(TypeError) as tz:    
    print('Exception due to :',tz)
except(ValueError) as tz:    
    print('Exception due to :',tz)
except(IOError) as tz:    
    print('Exception due to :',tz)  
except:
    print('Exception  : ') 


print()
print('Rest of the code...')



