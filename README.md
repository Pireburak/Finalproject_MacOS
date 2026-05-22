<div align="center">

# 🕸️ Advanced WebRTC Network Reconnaissance Module

```text
__        __   _    ____ _____ ____   ____                                
\ \      / /__| |__|  _ \_   _/ ___| |  _ \ ___  ___ ___  _ __            
 \ \ /\ / / _ \ '_ \ |_) || || |     | |_) / _ \/ __/ _ \| '_ \           
  \ V  V /  __/ |_) |  _ <| || |___  |  _ <  __/ (_| (_) | | | |          
   \_/\_/ \___|_.__/|_| \_\_| \____| |_| \_\___|\___\___/|_| |_|          
                                                                          
Bilgi Güvenliği Teknolojileri - Akademik Konsept İspatı (PoC) ve Zafiyet Analizi

📑 Proje Özeti (Abstract)
Bu proje, modern web tarayıcılarında P2P (Peer-to-Peer) ses ve görüntü transferini sağlayan WebRTC (Web Real-Time Communication) teknolojisinin güvenlik zafiyetlerini analiz etmek amacıyla geliştirilmiştir.

WebRTC, cihazlar arası en düşük gecikmeli (low-latency) bağlantıyı kurabilmek için NAT (Network Address Translation) arkasındaki cihazların gerçek ağ arayüzlerini tarar. Bu durum, kullanıcı bir VPN (Virtual Private Network) veya Proxy kullansa dahi, gerçek Yerel (Local) ve Genel (Public) IP adreslerinin ifşa olmasına (Deanonymization) yol açar. Bu depo, söz konusu zafiyetin anatomisini, nasıl sömürülebildiğini ve modern sistemlerde nasıl yamalandığını incelemektedir.

⚙️ Zafiyetin Anatomisi (Vulnerability Mechanics)
Bu aracın çekirdek mimarisi, iki temel ağ protokolünün istismarına (exploitation) dayanır:

ICE (Interactive Connectivity Establishment): Cihazın kendi ağ kartındaki (NIC) arayüzleri tarayarak yerel IP bloklarını (192.168.x.x, 10.x.x.x) SDP paketine yazar.

STUN (Session Traversal Utilities for NAT): Dış ağdaki bir sunucuya (örneğin projede kullanılan stun.l.google.com) istek atarak, modemin/router'ın dış bacağındaki gerçek Public IP adresini tespit eder ve geri döndürür.

Aracımız, tarayıcıda sahte bir WebRTC veri kanalı (createDataChannel) oluşturarak bu protokolleri tetikler ve oluşan SDP (Session Description Protocol) paketini parçalayarak (parsing) IP adreslerini ayrıştırır.

📸 Ekran Görüntüleri (Screenshots)
[ÖNEMLİ] Bu aracı çalıştırdığınızda göreceğiniz arayüz aşağıdadır.

(Buraya kendi aracının ekran görüntüsünü sürükleyip bırakabilirsin. Örnek format:)
🚀 Gelişmiş Özellikler (v2.0)
Önceki sürümlerden farklı olarak bu modül, bir güvenlik analistinin ihtiyaç duyabileceği derinlemesine keşif (recon) verilerini sağlar:

[x] Client Fingerprinting: Hedef sistemin User-Agent verisini çekerek işletim sistemi ve tarayıcı tespiti.

[x] Public IP Resolution: Google STUN sunucuları üzerinden dış ağ ifşası.

[x] Raw Payload Extraction: Zafiyetin kaynağı olan oluşturulmuş Raw SDP veri paketini şifresiz olarak ekrana basma.

🛠️ Kurulum ve Test (Saldırı Simülasyonu)
Güncel işletim sistemleri ve tarayıcılar bu zafiyete karşı yamalanmıştır. Zafiyetin orijinal halini (Zero-day dönemi) simüle edebilmek için, test ortamındaki tarayıcının güvenlik katmanının kapatılması gerekmektedir.

Test Adımları (Mozilla Firefox Ortamı):
Tarayıcı adres çubuğuna about:config yazın ve enter'a basın.

Çıkan güvenlik uyarısında "Riski kabul et ve devam et" seçeneğini işaretleyin.

Arama çubuğuna şu değeri girin:
media.peerconnection.ice.obfuscate_host_addresses

Değeri true durumundan çift tıklayarak false durumuna getirin.

Bu depodaki webrtc_zafiyeti.html dosyasını tarayıcıda açın veya yerel bir sunucuda (localhost) çalıştırın.

🛡️ Savunma Mimarisi: mDNS Obfuscation (Mitigation)
Bu projenin en önemli akademik çıktılarından biri, zafiyete karşı geliştirilen savunma mekanizmasının analizidir. Başta Apple (macOS / Safari) olmak üzere modern sistemler, bu zafiyeti mDNS (Multicast DNS) kullanarak çözmüştür.

Eğer bu aracı korumaları açık güncel bir macOS sisteminde çalıştırırsanız:

Sistem, WebRTC'ye gerçek yerel IP adresi (192.168.1.10) yerine, rastgele üretilmiş tek kullanımlık bir UUID tabanlı .local adresi (örn: 1b8b2...local) tahsis eder.

Bu mimari sayesinde P2P iletişimi kopmaz, bağlantı sağlanır; ancak kullanıcının gerçek ağ kimliği (Privacy) %100 oranında korunmuş olur.

⚠️ Yasal Uyarı ve Etik Bildirim (Disclaimer)
Bu depo ve içerisindeki kodlar, yalnızca üniversite seviyesinde akademik araştırma, eğitim ve güvenlik sistemlerinin çalışma mantığını anlamak amacıyla geliştirilmiştir. Bilgi Güvenliği dersleri kapsamında bir savunma ve analiz (Blue Team/Red Team) projesidir. Araçların yetkisiz sistemlerde kullanılması ve kötüye kullanımından doğacak her türlü yasal sorumluluk son kullanıcıya aittir.

Bu format, hem bolca Markdown görseli (rozetler ve ASCII sanat) içerdiği hem de projeyi gerçek bir siber güvenlik araştırması gibi sunduğu için GitHub profilinde çok daha havalı duracaktır. Kodu GitHub'a yüklerken bu metni direkt kopyalayabilirsin!
