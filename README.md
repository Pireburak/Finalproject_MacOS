# 🎯 macOS Güvenlik Analizi ve Zafiyet Sömürü Seti

## 📋 Konu Özeti
Bu proje, bir siber güvenlik operasyonunun tüm yaşam döngüsünü uygulamalı olarak göstermektedir. Sistem iki ana aşamadan oluşur:
1. **Aktif Bilgi Toplama (Reconnaissance):** Hedef sistemin servis ve altyapı bilgileri ağ üzerinden tespit edilir.
2. **Zafiyet Sömürüsü (Exploitation):** macOS ve tarayıcı ortamında WebRTC protokolündeki güvenlik açığı kullanılarak, VPN/Proxy arkasındaki gerçek yerel IP adresi açığa çıkarılır.

Tüm bu süreç boyunca, işlemlerin arka planı ağ izleme araçlarıyla paket seviyesinde (TCP Flags) doğrulanmıştır.

## 📊 Operasyonel Akış Diyagramı

```mermaid
graph LR
    A[Hedef Belirleme] -->|Adım 1| B(recon.py ile Keşif)
    B -->|Adım 2| C{tcpdump ile Ağ Analizi}
    C -->|Adım 3| D[webrtc_zafiyeti.html ile Sömürü]
    D -->|Sonuç| E((IP İfşası ve Doğrulama))
sudo tcpdump -i any port 80 -vv
python3 recon.py <HEDEF_IP> <HEDEF_PORT>
