import os
import time

pilihan = input("Apakah tetap ingin melanjutkan? (Ya/Tidak)")
kata = pilihan.upper()

if kata == "YA":
    for i in range(10,0,-1):
        print("Komputer mati dalam "+ str(i))
        time.sleep(1)
    if i <= 1:
        # os.system("shutdown /r /t 2")
        print("haloooooooooo")
        print("baiiii")
    elif kata == "TIDAK":
        exit()