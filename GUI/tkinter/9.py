import tkinter 

from tkinter import messagebox

top = tkinter.Tk()
top.geometry("350x350")

def m1():
   messagebox.showinfo( "Micky mouse", "Disney World")

B = tkinter.Button(top, text = "Micky", command = m1, height = 10, width = 20, bg="lightblue", fg="green")
B.place(x = 50,y = 50)

top.mainloop()
