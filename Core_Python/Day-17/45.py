# exception

try:
    a = int(input('Enter user value : '))   #abc
    try:
        print('upper try')
        print(10/a)
    except ZeroDivisionError as ze:
        print('Exception : ',ze)
except:
    try:
        print('lower try')
        print(10/2)
    except:
        print('Lower Exception...')
    else:
        print('lower Else..')
else:
    print('outer else..')                            

    