from tkinter import *

window = Tk()

window.title("Welcome to ATS")
window.geometry('350x200')

lbl = Label(window, text="ATH")
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

def clicked():
    res = "Welcome to " + txt.get()+" Session"
    lbl.configure(text= res)
    print('Data entered is : ',txt.get())

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()
