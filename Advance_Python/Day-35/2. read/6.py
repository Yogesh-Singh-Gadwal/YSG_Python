# File Handling
from time import sleep

myfile = open('myone.txt',"rt")

for x in myfile:
    sleep(1)
    print('****  ->   ',x)




