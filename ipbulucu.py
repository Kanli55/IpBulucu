import socket
import os
os.system("clear")
os.system("pkg install figlet")
os.system("clear")
os.system("figlet Ip Bulucu")
print("______#codded by KanlıSilah_____")
def site_ip_bul(alan_adı):
    try:
        ip_adresi = socket.gethostbyname(alan_adı)
        print(f"Site IP adresi: {ip_adresi}")
    except socket.gaierror:
        print("Hata: IP adresi bulunamadı.")

# Kullanım örneği:
alan_adı = input("Web sitesinin alan adını girin:\nİnput website url: ")
site_ip_bul(alan_adı)
