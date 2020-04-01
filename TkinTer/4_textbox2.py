import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Copy ........... past')

aLabel =ttk.Label(win, text = 'Enter file name')
aLabel.grid(column = 0, row = 0)


def clickMe():
    try:
        file_name1 = name.get()
        with open(file_name1) as file:
            f1 = file.read()
        file_name2 = name1.get()
        f2 = open(file_name2, 'w')
        aLabel.configure(foreground = 'green')
        action.configure(f2.write(f1))
        f2.close()
        
    except :
        action.configure(text = 'Ok file has been copyed ...')
        with open(file_name2) as file:
            f2 = file.read()
        action.configure(text = f2)


action = ttk.Button(win,text = 'click to copy', command = clickMe)
action.grid(column = 1, row = 1)
name = tk.StringVar()
name1 = tk.StringVar()
textbox = ttk.Entry(win, width = 12, textvariable = name)
textbox.grid(column = 0, row = 1)
textbox2 = ttk.Entry(win, width = 12, textvariable = name1)
textbox2.grid(column = 0, row = 2)

win.mainloop()
