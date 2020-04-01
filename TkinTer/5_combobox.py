import tkinter as tk
from tkinter import ttk
 

win = tk.Tk()
win.title('combobox')

aLabel = ttk.Label(win, text = 'Enter a name: ').grid( column = 0, row = 0)
aLabel2 = ttk.Label(win, text = 'Choose a number:').grid( column = 1, row = 0)

def clickMe():
    action.configure(text = 'Hello {} : {}'.format(name.get(), number.get()))
    aLabel.configure(foreground = 'yellow')


action = ttk.Button(win, text = 'Click me', command = clickMe)
action.grid(column = 2, row = 1)

name = tk.StringVar()
textbox = ttk.Entry(win, width = 12, textvariable = name)
textbox.grid(column = 0, row = 1)

number = tk.StringVar()
numberbox = ttk.Combobox(win, width = 12, textvariable = number)

numberbox['values' ] = (1, 2, 3, 4, 5, 6, 7, 45, 63)
numberbox.current(0)

numberbox.grid(column = 1, row = 1)



win.mainloop()