import tkinter as tk
root = tk.Tk()
root.geometry("400x200")

textEntry = tk.StringVar()
textEntry.set("Default Text")
textExample = tk.Entry(root,
                      textvariable = textEntry)

textExample.pack()

root.mainloop()


