from tkinter import *

root = Tk()

var = StringVar()
label = Label(root, textvariable = var, relief = RAISED)
var.set("Hello Micky, how are you ? ..")
label.pack()

root.mainloop()

