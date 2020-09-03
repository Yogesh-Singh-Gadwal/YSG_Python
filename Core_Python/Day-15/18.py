# recursive funx

import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(500)

print(sys.getrecursionlimit())


# recursive func
cu = 0
def m1():
    global cu
    cu += 1
    print('Micky : ',cu)
    m1()

m1()
