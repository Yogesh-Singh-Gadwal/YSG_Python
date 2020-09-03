# recursive funx

def myfun(num):
    if num == 0:
        print('Count completed...')
    else:
        print(num)
        myfun(num-1)

myfun(7)

