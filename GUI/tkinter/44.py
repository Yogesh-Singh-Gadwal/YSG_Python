import tkinter as tk  
from functools import partial  
from tkinter import *   
   
def call_result(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)  
    return  
   
root = tk.Tk()  
root.geometry('400x200+100+200')  
  
root.title('Calculator')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
  
tk.Label(root, text="A").grid(row=1, column=0)    
tk.Label(root, text="B").grid(row=2, column=0)  
  
labelResult = tk.Label(root)   
labelResult.grid(row=7, column=2)  
  
tk.Entry(root, textvariable=number1).grid(row=1, column=2)    
tk.Entry(root, textvariable=number2).grid(row=2, column=2)  
  
call_result = partial(call_result, labelResult, number1, number2)  
  
tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)  
  
root.mainloop()  
