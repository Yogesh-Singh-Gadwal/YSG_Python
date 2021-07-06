from tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Disney World.....")
text.pack()

#-------------------(Start index,end index)           
text.tag_add("start", "1.0", "1.8")
text.tag_add("end", "1.10", "1.16")
text.tag_config("start", background = "yellow", foreground = "blue")
text.tag_config("end", background = "orange", foreground = "green")
root.mainloop()

