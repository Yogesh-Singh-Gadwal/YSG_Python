# Exception

try:
    a = int(input('Enter user value : '))
    print(10/a)
    print('Micky'+a)
except(ZeroDivisionError,TypeError,ValueError) as tz:
    print()
    print('Exception due to :',tz)

print()
print('Rest of the code...')



