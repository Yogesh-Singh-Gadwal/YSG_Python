from tkinter import *
from tkinter import Menu

window = Tk()
window.title("Welcome to ATS")

menu = Menu(window)
#new_item = Menu(menu, tearoff = 0)
new_item = Menu(Menu)

def result():
    print('You Have Selected NEW button Command')
    
new_item.add_command(label='New',command=result)
menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)

window.mainloop()
