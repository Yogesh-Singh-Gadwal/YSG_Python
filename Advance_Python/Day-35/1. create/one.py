# File Handling

#myfile = open('myonefile.txt','rt')   # FileNotFoundError: [Errno 2] No such file or directory: 'myonefile.txt'

#myfile = open('myone.txt','rt')   
#print(myfile)

#myfile = open('mytwo.txt','a')

#myfile = open('mythree.txt','w')

#myfile = open('myfour.txt','x')  

myfile = open('myfour.txt','x')    # FileExistsError: [Errno 17] File exists: 'myfour.txt'


