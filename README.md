# 🎯 macOS Güvenlik Analizi ve Zafiyet Sömürü Seti

## 📋 Konu Özeti
Bu proje, bir siber güvenlik operasyonunun tüm yaşam döngüsünü uygulamalı olarak göstermektedir. Sistem iki ana aşamadan oluşur:
1. **Aktif Bilgi Toplama (Reconnaissance):** Hedef sistemin servis ve altyapı bilgileri ağ üzerinden tespit edilir.
2. **Zafiyet Sömürüsü (Exploitation):** macOS ve tarayıcı ortamında WebRTC protokolündeki güvenlik açığı kullanılarak, VPN/Proxy arkasındaki gerçek yerel IP adresi açığa çıkarılır.

Tüm bu süreç boyunca, işlemlerin arka planı ağ izleme araçlarıyla paket seviyesinde (TCP Flags) doğrulanmıştır.

## 📊 Operasyonel Akış Diyagramı

```mermaid
graph LR
    A[Hedef Belirleme] --> B[recon.py ile Kesif]
    B --> C[tcpdump ile Ag Analizi]
    C --> D[webrtc ile Somuru]
    D --> E((IP Ifsasi))
