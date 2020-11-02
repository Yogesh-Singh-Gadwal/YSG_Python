# File Handling
from time import sleep

myfile = open('mytwo.txt',"w")
myfile.write("*"*40)
myfile.write("\n")
sleep(2)
for x in range(7):
    sleep(2)
    myfile.write(' \n This is Micky From Disney World : ')

myfile.write("\n")
myfile.write("*"*40)





