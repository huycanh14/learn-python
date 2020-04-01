import tkinter as tk
from tkinter import ttk

win = tk.Tk();
win.title('python ckeck button')

chavar = tk.IntVar()

check1 = tk.Checkbutton(win, text = 'Enable', variable = chavar, state = 'disabled')
check1.select()
check1.grid(column = 0, row = 0, sticky = tk.W)
chavar2 = tk.IntVar()
check2 = tk.Checkbutton(win, text = 'Disable', variable = chavar2)
check2.deselect()
check2.grid(column = 1, row = 0)



win.mainloop()
