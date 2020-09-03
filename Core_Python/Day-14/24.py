# Function
# arguments and parameters

# default arguments

def status(name,phone):
    print('User name : ',name)
    print('User phone : ',phone)

status('micky',998877)


print()


# default arguments

def status2(name,phone=0):
    print('User name : ',name)
    print('User phone : ',phone)

status2('micky')

print()

# default arguments

def status3(name,phone=0):
    print('User name : ',name)
    print('User phone : ',phone)

status3('micky',887788)

