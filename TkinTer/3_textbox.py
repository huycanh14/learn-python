import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python tkinter')
aLable = ttk.Label(win, text='Enter a name:')
aLable.grid(column=0, row=0)

def clickMe():
    file_name = name.get()
    with open(file_name) as file:
        f = file.read()

    
    action.configure(text=f)
    aLable.configure(foreground='green')


action = ttk.Button(win, text='click me', command=clickMe)
action.grid(column=1, row=1)

name = tk.StringVar()

textbox = ttk.Entry(win, width=12, textvariable=name)
textbox.grid(column=0, row=1)


win.mainloop()
