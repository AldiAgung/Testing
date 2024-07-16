import os
import time
import random

pilihan = input("Apakah tetap ingin melanjutkan? (Ya/Tidak)")
kata = pilihan.upper()


if kata == "YA":
    for i in range(3,0,-1):
        print("Komputer mati dalam "+ str(i))
        time.sleep(1)
        if i <= 1:
            print("tapi aku masih bakalan kasih kesempatan satu kali lagi")
            time.sleep(2)
            print("jika bener jawabannya, gabakalan ke restart")
            time.sleep(2)
            print("kalau salah yah tetep aja ke restart lmao")
            time.sleep(2)
            print("siap?")
            time.sleep(2)
            tebak = input("tebak angkanya: ")
            angka = random.randrange(1,10)
            if (tebak != angka):
                print("sayang sekali jawaban kamu salah")
                time.sleep(2)
                print("jawabannya adalah: "+ str(angka))
                time.sleep(2)
                print("jadi sekarang pc kamu ke restart deh, hahahhaha")
                time.sleep(2)
                os.system("shutdown /r /t 10")
                berkas = open('Halopy', 'w')
                berkas.write("laptop kamu mati hahah")
            else:
                print("jawaban yang benar adalah: "+ str(angka))
                print("selamat pc kammu tidak ke restart")
                time.sleep(2)
                exit()
elif kata == "TIDAK":
    exit()