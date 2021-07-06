import tkinter as tk

top = tk.Tk()
def close_window():
    global entry
    entry = E1.get()
    print('Result is : ',entry)
    top.destroy()
    
L1 = tk.Label(top, text = "Enter User Name : ")
L1.pack(side = tk.LEFT)

E1 = tk.Entry(top, bd = 5)
E1.pack(side = tk.RIGHT)

B = tk.Button(top, text = "OK", command = close_window)
B.pack(anchor = tk.S)

top.mainloop()
