# loops
# patterns

'''

    *
   * *
  * * *
 * * * *
* * * * *

'''

v1 = int(input('Enter user value : '))

for x in range(v1):
    for y in range(v1-x-1):
        print(' ',end='')
    for y in range(x+1):
        print('*',end=" ")
    print()    

