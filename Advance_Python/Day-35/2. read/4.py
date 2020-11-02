# File Handling
import time 
myfile = open('myone.txt',"rt")
print(myfile.readline())


time.sleep(3)
print('')
print('****'*40)
print('')

myfile2 = open('myone.txt',"rt")
print(myfile2.readline())
print(myfile2.readline())
print(myfile2.readline())

