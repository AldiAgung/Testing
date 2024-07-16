from tkinter import *
import tkinter as tk
from ttkbootstrap.constants import *
# from tkFileDialog import *
# from server import hubungkan

# port = 5050
m = Tk()
m.geometry('800x600')
m.title("Hallooooo")
status = Label(m, text= 'Status internet: ').grid(row = 0)
tombol = Button(m, text= 'sentuh aku', command = m.destroy) # , width= 25, command= m.get(hubungkan))
box1 = Entry(m)

# Peletakan tombol dan semacamnya #
# tombol.grid(column= 0, row= 0)
tombol.grid(row = 1, column= 1)
box1.grid(row = 0, column= 1)

# tombol.pack()
# namalabel.pack()
m.mainloop()