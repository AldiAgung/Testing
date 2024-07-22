from tkinter import *
# from tkFileDialog import *
from server import hubungkan, alamatip
import os, datetime

#inisiasi variable
# port = 5050
m = Tk()
# m.geometry('800x600')
m.title("Hallooooo")
m.frame()
m.grid()

def convert(event):
    alamatip

def update(mystring):
    update.set(mystring)

label_ip = Label(m, text= 'Ip Internet: '+ str(alamatip)).grid(row = 0, column= 0)
status_internet = Label(m, text= 'Status internet: ').grid(row = 1, column= 0)
tombol_refresh = Button(m, text= "Refresh")
# tombol_refresh = Button(m, text= 'refresh', c) # , width= 25, command= hubungkan()))
tombol_refresh.bind("<Button-1>", convert)
updatehasil = StringVar(m)
# status_internet = print(status)

# Peletakan tombol dan semacamnya #
# tombol.grid(column= 0, row= 0)
tombol_refresh.grid(row = 3, column= 0)
# status_internet.grid(row = 0, column= 1)

# tombol.pack()
# namalabel.pack()
if __name__ == "__main__":
    m.mainloop()