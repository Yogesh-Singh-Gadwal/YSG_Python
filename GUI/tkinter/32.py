from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Welcome to ATS")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')
tab_control.pack(expand=1, fill='both')

window.mainloop()
