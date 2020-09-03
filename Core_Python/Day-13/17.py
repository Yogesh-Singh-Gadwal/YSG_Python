# function 

# ((500+200)-300)(*(5)) 
# = 700 -300 (*(5)) 
# = 400 (*(5)) 
# = 400 * 5
#  2000
def addition():
    a = 500
    b = 200
    return a+b

def sub():
    c = 300
    v1  = addition()
    d = v1 - c  
    return d   

def mul():
    e = 5
    res = sub() * e 
    return res

print('Final Result is : ',mul())    



