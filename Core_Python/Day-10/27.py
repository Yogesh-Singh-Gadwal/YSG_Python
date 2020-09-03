# loops
# patterns
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''
'''
v1 = int(input('Enter user value : '))
for x in range(v1):
    for y in range(x+1):
        print(x+y+1,end=" ")
    print() 
'''

v1 = int(input('Enter user value : '))
a = 1
for x in range(v1):
    for y in range(x+1):
        print(a,end=" ")
        a += 1
    print() 



