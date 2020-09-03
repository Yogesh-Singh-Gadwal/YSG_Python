# Function
# arguments and parameters

# default arguments

def indiamart(pro1=0.0,pro2=0.0,pro3=0.0,gst=0.02):
    print('Product -1 cost is : ',pro1)
    print('Product -2 cost is : ',pro2)
    print('Product -3 cost is : ',pro3)
    print('GST value is : ',gst)
    print()
    print('*'*20)
    print('Tax Amount is : ',((pro1+pro2+pro3)*gst))
    print('Total Amount is : ',(pro1+pro2+pro3)+((pro1+pro2+pro3)*gst))

v1 = 100
v2 = 23
v3 = 89
indiamart(v1,v2,v3)
