from tkinter import *
from tkinter import messagebox
from ip_grab import alamatip, interstatus
import os
from datetime import datetime

#inisiasi variable
m = Tk()
# m.geometry('800x600')
m.title("Hallooooo")
m.frame()
m.grid()
waktu_lokal = datetime.now().strftime('%H:%M:%S')

# Fungsi #
def refresh():
    m.destroy()
    os.system(__file__)

def lihatip():
    try:
        alamat = alamatip()
        if alamat:
            label_ip.config(text= f'{alamat}')
    except Exception as e:
        messagebox.showerror("Terjadi kesalahan", str(e))

def status():
    try:
        kondisi = interstatus()
        if kondisi:
            label_status.config(text= f'Terhubung')
        else:
            label_status.config(text= f'Tidak terhubung')
    except Exception as e:
        messagebox.showerror("Terjadi kesalahan", str(e))

# inisiasi label dll
Label(m, text= 'Ip Internet: ').grid(row = 0, column= 0, pady = 5, padx= 5, sticky='w')
Label(m, text= 'Status internet: ').grid(row = 1, column= 0, pady= 5, padx= 5, sticky= 'w')
label_ip = Label(m, text= "")
label_status = Label(m, text= "")

#lokasi tombol
label_status.grid(row = 1, column= 1, pady= 5, sticky= 'w')
label_ip.grid(row=0, column=1, pady=5, sticky= 'w')
waktu_lokal = Label(m, text= f"Waktu lokal: {waktu_lokal}").grid(row= 2, column= 0, columnspan= 2, padx= 5, pady= 5, sticky= 'w')

## Tombol ##
tombol_refresh = Button(m, text= "Refresh", command= refresh).grid(row = 3, column= 0, columnspan= 2, pady= 10)

if __name__ == "__main__":
    lihatip()
    status()
    m.mainloop()