import sys

sys.path.append('D:/set2/pk1')

import time
# 1st 
time.sleep(2)

import C
v1 = float(input('Enter pro1 cost : '))
v2 = float(input('Enter pro2 cost : '))
v3 = float(input('Enter pro3 cost : '))
v4 = float(input('Enter pro4 cost : '))
print()
C.demart(v1,v2,v3,v4)
print()
print()

input()
time.sleep(3)
# 2nd way

from A import book

v1 = input('Enter Book name : ')
v2 = input('Enter Book cost : ')
print()
book(v1,v2)


input()
time.sleep(3)
# 3rd

print()
print()

import B as ks
v1 = float(input('Enter amount to deposite : '))
print()
ks.deposite(v1)

input()
time.sleep(3)
# 4th
print()
print()


import D 
v1 = float(input('Enter amount to withdraw : '))
print()
D.withdraw(v1)









