# recursive funx

def myfun(num):
    if num == 0:
        return 0
    else:
        return num + myfun(num-1)

print('Result is : ',myfun(10))





