# loops
# patterns

'''
A             65
B B           66
C C C         67 
D D D D       68
E E E E E     69

'''

v1 = int(input('Enter user value : '))
a = 0
for x in range(v1):
    for y in range(x+1):
        value = chr(65+a)
        print(value,end=" ")
    a+=1
    print()    



# HW

'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

'''

