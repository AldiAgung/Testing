from tkinter import *
import tkinter as tk
# from tkFileDialog import *
from server import status, hubungkan

# port = 5050
m = Tk()
m.geometry('800x600')
m.title("Hallooooo")
m.frame()

Ip_address = Label(m, text= 'Ip Internett: ' {}).grid(row = 0)
status_internet = Label(m, text= 'Status internet: ').grid(row = 1)
tombol = Button(m, text= 'refresh', command = m.destroy) # , width= 25, command= hubungkan()))
# status_internet = print(status)

# Peletakan tombol dan semacamnya #
# tombol.grid(column= 0, row= 0)
tombol.grid(row = 1, column= 1)
# status_internet.grid(row = 0, column= 1)

# tombol.pack()
# namalabel.pack()
m.mainloop()