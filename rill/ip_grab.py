import socket

port = 80
host = "www.google.com"
# def hubungkan():
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         print("terbuat socket")
#     except socket.timeout as err:
#         print("Tidak bisa dijalankan karena: %s" %(err))
#         # connecting to the server
#         host_ip = socket.gethostbyname('www.google.com')
#         s.connect(host_ip, port)
#         s.send(1024)
#     sys.exit()

def alamatip():
    try:
        namahost = socket.gethostname()
        ipaddress = socket.gethostbyname(namahost)
        return ipaddress
    except socket.gaierror as gada:
        print(f'Tidak ada koneksi internet yang valid {gada}')

def interstatus():
    try:
        socket.setdefaulttimeout(4)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        alamatserver = (host, port)
        s.connect(alamatserver)
        s.close()
        return True
    except OSError:
        return False
