import os
import time

for i in range(10,0,-1):
    print("Komputer mati dalam "+ str(i))
    if i <= 1:
        os.system("shutdown /r /t 0")
        print("baiiii")
    time.sleep(1)