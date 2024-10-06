from tkinter import *
# from tkFileDialog import *
from server import hubungkan, alamatip
import os
from datetime import datetime

#inisiasi variable
# port = 5050
m = Tk()
# m.geometry('800x600')
m.title("Hallooooo")
m.frame()
m.grid()
waktu_lokal = datetime.now().strftime('%H:%M:%S')
waktu_awal = waktu_lokal

# def convert(nama):
#     alamatip.__name__

# def kembali(self):
#     d

def refresh():
    m.destroy()
    os.popen(__name__)

def update(mystring):
    update.set(mystring) 

# inisiasi label dll
label_ip = Label(m, text= 'Ip Internet: '+ str(alamatip.__name__)).grid(row = 0, column= 0)
status_internet = Label(m, text= 'Status internet: ').grid(row = 2, column= 0)
waktu_awal = Label(m, text= 'Waktu sekarang '+ str(waktu_lokal)).grid(row= 1, column= 0)
waktu_akhir = Label(m, text= 'Tere')
tombol_refresh = Button(m, text= "Refresh", command= refresh)
# tombol_refresh.bind("<Button-1>", convert)
# updatehasil = StringVar(m)
# status_internet = print(status)

# Peletakan tombol dan semacamnya #
tombol_refresh.grid(row = 3, column= 0)
# tombol.pack()
# namalabel.pack()

if __name__ == "__main__":
    m.mainloop()