import tkinter as tk
    
def write_slogan():
    print("Hi this is Micky Mouse")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="Micky",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
