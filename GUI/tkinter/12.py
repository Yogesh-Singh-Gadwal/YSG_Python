import tkinter
 
root =tkinter.Tk()
i=tkinter.IntVar()

c = tkinter.Checkbutton(root, text = "Python", variable=i,height=5,width = 20,)
c.pack()
 
def click_me():
    print('YOu have selected python option : ',i.get())

b = tkinter.Button(root,text="Click here",command=click_me)
b.pack()
 
root.geometry("300x200+120+120")
root.mainloop()
