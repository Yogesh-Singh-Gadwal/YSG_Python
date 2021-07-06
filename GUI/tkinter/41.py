from tkinter import *

m1 = PanedWindow()
m1.pack(fill = BOTH, expand = 1)

left = Entry(m1)
m1.add(left)

m2 = PanedWindow(m1, orient = VERTICAL)
m1.add(m2)

var = DoubleVar()
top = Scale( m2, variable = var, orient = HORIZONTAL)
m2.add(top)

def sel():   
   selection = "Value = " + str(var.get())+' - '*2
   left.insert(0,selection)      
   print(str(var.get()))
   

bottom = Button(m2, text = "OK", command=sel)
m2.add(bottom)

mainloop()

