import tkinter
    
top = tkinter.Tk()

C1 = tkinter.Checkbutton(top, text = "Car",offvalue = 0, height=5,width = 20)
C1.pack()

C2 = tkinter.Checkbutton(top, text = "Bike",offvalue = 0, height=5,width = 20)
C2.pack()

top.mainloop()
