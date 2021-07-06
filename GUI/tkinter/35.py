from tkinter import *

root = Tk()

var = StringVar()
label = Message( root, textvariable = var, relief = RAISED )

var.set("Hello micky, How are you ?")
label.pack()
root.mainloop()

