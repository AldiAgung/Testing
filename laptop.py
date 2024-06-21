import os

try:
    kata =  int(input("berapa lama?: "))
    os.system('shutdown /s /t '+ str(kata))
except ValueError:
    print(f"Harus berupa sebuah angka")