from tkinter import *
import tkinter as tk
from ttkbootstrap.constants import *
# from tkFileDialog import *
# from server import hubungkan

# port = 5050
m = Tk()
# m.geometry('800x600')
m.title("Hallooooo")
namalabel = Label(m, text= 'Halloooo')
tombol = Button(m, text= 'sentuh aku') # , width= 25, command= m.get(hubungkan))
tombol.grid(column= 0, row= 0)

tombol.pack()
namalabel.pack()
m.mainloop()