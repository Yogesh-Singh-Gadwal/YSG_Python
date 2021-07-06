import tkinter

window = tkinter.Tk()

window.title("This is Micky")

window.geometry('350x200')

lbl = tkinter.Label(window, text="Micky")
lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Welcome to Micky Class !!")

btn = tkinter.Button(window, text="My-Button", command=clicked)
btn.grid(column=1, row=0)

window.mainloop()
