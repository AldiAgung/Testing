import os
import time

pilihan = input("Apakah tetap ingin melanjutkan? (Ya/Tidak)")
if pilihan == "Ya":
    for i in range(10,0,-1):
        print("Komputer mati dalam "+ str(i))
        time.sleep(2)
    if i <= 1:
        os.system("shutdown /r /t 2")
        # print("haloooooooooo")
        print("baiiii")
    elif pilihan == "Tidak":
        exit()