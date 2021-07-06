import tkinter

master = tkinter.Tk()

def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

tkinter.Label(master, text="Your sex:").grid(row=0, sticky=tkinter.W)

var1 = tkinter.IntVar()
tkinter.Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=tkinter.W)

var2 = tkinter.IntVar()
tkinter.Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=tkinter.W)

tkinter.Button(master, text='Quit', command=master.quit).grid(row=3, sticky=tkinter.W, pady=4)
tkinter.Button(master, text='Show', command=var_states).grid(row=4, sticky=tkinter.W, pady=4)

tkinter.mainloop()
