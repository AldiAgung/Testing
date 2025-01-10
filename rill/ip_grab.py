import socket, sys

port = 5050
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
        print(f'Tidak koneksi internet yang valid {gada}')

# def status():
    