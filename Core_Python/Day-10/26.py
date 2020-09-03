# loops
# patterns

'''

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''
'''
v1 = int(input('Enter user value : '))
a = 1
for x in range(v1):
    print('1 '*a)
    a +=1
'''

v1 = int(input('Enter user value : '))
for x in range(v1):
    for y in range(x+1):
        print(y+1,end=" ")
    print() 

