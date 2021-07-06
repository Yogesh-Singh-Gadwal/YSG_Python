import tkinter
window = tkinter.Tk()
window.title("ATH")
window.geometry('350x200')
lbl = tkinter.Label(window, text = "Micky Data")
lbl.grid(column =0, row = 2)
btn = tkinter.Button(window, text = "Button-1", bg = "lightblue", fg = "green")
btn.grid(column =1, row =0)
window.mainloop()
