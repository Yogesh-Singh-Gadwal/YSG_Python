from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("ATH")

window.geometry('350x200')

combo = Combobox(window)

combo['values']= ("Micky", "ATS", "INDIA", "PYTHON", "CODE", "Text")

combo.current(1) #set the selected item

combo.grid(column=0, row=0)
print(combo.get())

window.mainloop()

