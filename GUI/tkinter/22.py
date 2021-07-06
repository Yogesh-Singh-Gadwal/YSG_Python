from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk
import tkinter as tk
root = Tk()
root.geometry("300x200")
# width - heghit window

cmb = ttk.Combobox(root, width="10", values=("Micky","India","ATS","Disney"))
#cmb = Combobox

def checkcmbo():
    if cmb.get() == "Micky":
        messagebox.showinfo("What user choose", "you choose MICKY")
    elif cmb.get() == "India":
        messagebox.showinfo("What user choose", "you choose INDIA")
    elif cmb.get() == "ATS":
        messagebox.showinfo("What user choose", "you choose ATS")
    elif cmb.get() == "Disney":
        messagebox.showinfo("What user choose", "you choose DISNEY")
    elif cmb.get() == "":
        messagebox.showinfo("nothing to show!", "you have to be choose something")

cmb.place(relx="0.1",rely="0.1")

btn = ttk.Button(root, text="Get Value",command=checkcmbo)
btn.place(relx="0.5",rely="0.1")

root.mainloop()
