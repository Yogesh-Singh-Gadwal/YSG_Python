from tkinter import *

def close_window():
    global entry
    entry = E.get()
    print('Value is : ',entry)
    root.destroy()

root = Tk()
E = Entry(root)
E.pack()

B = Button(root, text = "OK", command = close_window)
B.pack()

root.mainloop()
