# Exception Handling
# Abnormal termination

try:
    print('micky'+10)
except:
    print('micky'+10)
    try:
        print(10/0)    # TypeError: can only concatenate str (not "int") to str
    except:
        print('Inner Except...')

print('Rest of the code...')


