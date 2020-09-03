# Exception Handling
# normal termination

try:
    print('micky'+10)
except:
    try:
        print(10/0)
    except:
        print('Inner Except...')

print('Rest of the code...')


