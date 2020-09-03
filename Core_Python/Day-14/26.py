# Rules

# deafult with Required

def m1(pro1,pro2,pro3,gst=0.02):           # valid
    pass

def m2(pro1,pro2,pro3=50.0,gst=0.02):           # valid
    pass

def m3(pro1,pro2=30,pro3=50.0,gst=0.02):           # valid
    pass

def m4(pro1=10,pro2=45,pro3=50,gst=0.02):           # valid
    pass

# ----------------------------------------------------------- 

def m5(pro1=10,pro2=45,pro3=50,gst):           # Invalid
    pass

def m6(pro1=10,pro2=45,pro3,gst):              # Invalid
    pass

def m7(pro1=10,pro2,pro3,gst):                 # Invalid
    pass

def m8(pro1=10,pro2,pro3=50,gst):              # Invalid
    pass

def m9(pro1,pro2=45,pro3=50,gst):              # Invalid
    pass

def m10(pro1,pro2,pro3=50,gst):                # Invalid
    pass



