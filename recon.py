import socket
import time
import sys
from colorama import init, Fore, Style

# Renkli terminal çıktıları için
init(autoreset=True)

def print_banner():
    print(Fore.CYAN + """
      ███╗   ███╗ █████╗  ██████╗ ██████╗ ███████╗
      ████╗ ████║██╔══██╗██╔════╝██╔═══██╗██╔════╝
      ██╔████╔██║███████║██║     ██║   ██║███████╗
      ██║╚██╔╝██║██╔══██║██║     ██║   ██║╚════██║
      ██║ ╚═╝ ██║██║  ██║╚██████╗╚██████╔╝███████║
      ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
    """)
    print(Fore.YELLOW + "    macOS Recon & Banner Grabbing Engine v1.0")
    print(Fore.YELLOW + "    [Blue Team - Eğitim Amaçlı Bilgi Toplama Aracı]\n")

def grab_banner(target_ip, target_port):
    """Hedef porta bağlanır ve çalışan servisin imzasını (banner) çeker."""
    print(Fore.BLUE + f"[*] Hedef {target_ip}:{target_port} üzerinde keşif başlatılıyor...")
    time.sleep(1)
    
    # Zararsız bir keşif paketi (Probe) - Sisteme kim olduğunu sorar
    probe_payload = b"HEAD / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n"

    try:
        print(Fore.BLUE + f"[*] TCP soketi oluşturuluyor ve bağlantı deneniyor...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3) # 3 saniye zaman aşımı
        
        s.connect((target_ip, int(target_port)))
        print(Fore.GREEN + f"[+] BAĞLANTI BAŞARILI! Port {target_port} açık.")
        time.sleep(1)
        
        print(Fore.BLUE + "[*] Zararsız keşif paketi (Probe) gönderiliyor...")
        s.send(probe_payload)
        
        print(Fore.BLUE + "[*] Sistemden gelen yanıt bekleniyor...\n")
        # Karşıdan gelen ilk 1024 byte'ı (banner'ı) oku
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        
        print(Fore.MAGENTA + "================ SERVER BANNER ================")
        if banner:
            print(Fore.WHITE + banner)
        else:
            print(Fore.YELLOW + "[!] Servis yanıt vermedi (Sessiz modda veya farklı bir protokol bekliyor).")
        print(Fore.MAGENTA + "===============================================")
        
        s.close()
        
    except ConnectionRefusedError:
        print(Fore.RED + f"[-] HATA: {target_ip}:{target_port} bağlantıyı reddetti (Port kapalı).")
    except socket.timeout:
        print(Fore.RED + f"[-] HATA: Zaman aşımı! Güvenlik duvarı (Firewall) bağlantıyı engelliyor olabilir.")
    except Exception as e:
        print(Fore.RED + f"[-] BEKLENMEYEN HATA: {e}")

def main():
    print_banner()
    
    while True:
        print(Fore.CYAN + "\n--- HEDEF BELİRLEME ---")
        hedef_ip = input("Keşif Yapılacak Hedef IP (Çıkış için 'q'): ")
        
        if hedef_ip.lower() in ['q', 'exit', 'çıkış']:
            print(Fore.YELLOW + "\n[*] Keşif motoru kapatılıyor. Güvenli günler!")
            break
            
        hedef_port = input("Hedef Port (Örn: 22(SSH), 80(HTTP), 548(macOS AFP)): ")
        
        if not hedef_port.isdigit():
            print(Fore.RED + "\n[!] Lütfen geçerli bir port numarası girin.")
            continue
            
        grab_banner(hedef_ip, hedef_port)

if __name__ == "__main__":
    main()
