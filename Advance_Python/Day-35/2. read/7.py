# File Handling
import time
myfile = open('myone.txt',"rt")
print(myfile.readline())
print('India')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())

print('')
print('****'*40)
print('')
time.sleep(5)


myfile2 = open('myone.txt',"rt")
print(myfile2.readline())
print('India')
print(myfile2.readline())
print(myfile2.readline())
myfile2.close()            # ValueError: I/O operation on closed file.
print(myfile2.readline())
print(myfile2.readline())
print(myfile2.readline())

