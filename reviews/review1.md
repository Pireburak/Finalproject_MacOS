## 1. Teknik Özet (Executive Summary)

Bu proje, modern web tarayıcılarında çalışan **WebRTC (Web Real-Time Communication)** protokolünün ağ keşif süreçlerini manipüle ederek, kullanıcının gerçek ağ kimliğini (Yerel/Local ve Genel/Public IP adreslerini) ifşa etmeye yarayan bir **Keşif (Reconnaissance) ve Dekononimizasyon (Deanonymization)** PoC (Proof of Concept) çalışmasıdır.

### Temel Çalışma Mantığı (The Mechanics)

Normal şartlarda tarayıcı korumalı bir kum havuzunda (sandbox) çalışır ve yerel ağ kartınızın (NIC) IP adreslerine doğrudan erişemez. Ancak WebRTC, tarayıcılar arası doğrudan (P2P) ve en düşük gecikmeli ses/görüntü bağlantısını kurabilmek amacıyla **ICE (Interactive Connectivity Establishment)** protokolünü tetikler.

1.  **ICE ve SDP Üretimi:** Kod içerisinde sahte bir veri kanalı (`createDataChannel`) açıldığında tarayıcı, yerel ağ mimarisini çözmek için bir SDP (Session Description Protocol) paketi hazırlar. Bu paket, cihazın yerel ağdaki IP bloklarını şifresiz barındırır.

2.  **STUN Sunucuları:** Kod, Google'ın genel STUN sunucusuna (`stun:stun.l.google.com:19302`) istek atarak NAT (Router/Modem) arkasındaki cihazın dış bacağındaki **Gerçek Public IP** adresini öğrenir.

3.  **Regex ile Ayrıştırma:** JavaScript tarayıcı seviyesinde bu ham SDP çıktısını ve ICE adaylarını yakalar; basit bir Regex (`/([0-9]{1,3}(\.[0-9]{1,3}){3})/`) filtresinden geçirerek kullanıcının VPN veya Proxy arkasına gizlediği gerçek IP adreslerini ekrana basar.

---

## 2. Projenin Artıları (Güçlü Yanları)

- **Akademik Anlatım ve Yapı:** `README.md` ve `SECURITY.md` dosyaları bir akademik PoC projesine uygun, sorumluluk bilinciyle (responsible disclosure) ve temiz bir dille yazılmış . mDNS korumalarından bahsedilmesi teorik altyapının iyi kurulduğunu gösteriyor.

- **Dual-HTML Yapısı:** İlk HTML dosyası (`webrtc_zafiyeti.html`) tamamen yerel ağ adaylarına odaklanırken , ikinci dosya (`webrtc_zafiyeti2.html`) STUN sunucusu entegrasyonu ile Public IP tespitini ve ham SDP loglamasını başarıyla gerçekleştiriyor.

- **Görsel Tasarım (UI):** Siber güvenlik dünyasında "Cyberpunk/Terminal" temalı arayüzler (yeşil fontlar, siyah arka plan, veri kutuları) sunumlar ve ödev teslimleri için oldukça şık ve etkileyicidir.

---

## 3. Zafiyetler, Eksikler ve Kod Hataları

Projedeki dosyalar (özellikle HTML ve MacOSproject betiği) incelendiğinde, projenin kalitesini düşüren veya doğrudan **çalışma hatasına (runtime error)** sebep olan kritik noktalar tespit edilmiştir:

### A. Kod Hataları ve Syntax Problemleri (Kritik)

- **`MacOSproject` Dosyasında Sözdizimi Hatası (Syntax Error):**
  Python dosyasının 60. satırında `print(f"[+] GÜVENLİK DUVARI AŞILDI!` ifadesinden sonra alt satıra geçilmiş ancak string kapatılmamıştır. Python çok satırlı f-string'leri bu şekilde kabul etmez ve **`SyntaxError: EOL while scanning string literal`** hatası vererek programı doğrudan çökertir.

- **IPv6 Desteğinin Olmaması:**
  Her iki HTML dosyasındaki `ipRegex` ifadesi (`/([0-9]{1,3}(\.[0-9]{1,3}){3})/g`) yalnızca **IPv4** adreslerini yakalayabilir. Günümüzde özellikle mDNS kapalıysa veya modern mobil ağlarda WebRTC SDP paketleri yoğun şekilde **IPv6** adresi üretir. Mevcut kod bu adresleri tamamen kaçırır.

### B. Mantıksal ve Teknik Eksikler

- **Gereksiz / Çalışmayan Kod Blokları (`webrtc_zafiyeti.html`):**
  Kodun sonunda hem `pc.createOffer()` içinde SDP string'i split edilerek IP aranıyor, hem de `pc.onicecandidate` callback'i tanımlanmış. Ancak `pc.setLocalDescription(sdp, noop, noop)` çağrısı `createOffer`'ın hemen içinde (asenkron akış tam yönetilmeden) çağrıldığı için bazı tarayıcılarda `onicecandidate` tetiklenmeden akış bitebilir veya mükerrer (çift) tetiklenmelere sebep olur.

- **`MacOSproject` Dosyasının Proje ile Alakasızlığı:**

`README.md` tamamen WebRTC tabanlı bir tarayıcı zafiyetini anlatırken, `MacOSproject` adlı Python dosyası ağ üzerinden TCP soketi açıp statik bir Buffer Overflow payload'u gönderen tamamen farklı bir "Exploit" simülasyonudur. İki bağımsız konseptin aynı repoda net bir bağlam kurulmadan sunulması kafa karıştırıcıdır.

---

## 4. Ne Yapılabilir? (Geliştirme Yol Haritası)

Projenin akademik değerini artırmak ve production-grade bir siber güvenlik aracına dönüştürmek için şu adımlar atılmalıdır:

### 1. Python Kodundaki Syntax Hatasını Düzeltin

Python betiğindeki hatalı `print` fonksiyonunu tek satıra indirin veya üç tırnak (`"""`) kullanın:

```python
print(f"[+] GÜVENLİK DUVARI AŞILDI! {target_port} portu açık ve bağlantı kuruldu.")

```

### 2. Regex'i IPv6 Destekleyecek Şekilde Güncelleyin

Hem IPv4 hem de IPv6 adreslerini başarıyla parse edebilmek için JavaScript tarafındaki Regex mimarisini genişletin:

```javascript
const ipRegex =
  /([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9]{1,3}(\.[0-9]{1,3}){3})/g;
```

### 3. mDNS Bypass Araştırması Ekleyin (Akademik Katkı)

`README.md` dosyasında mDNS korumasından bahsedilmiş. Ancak yerel IP'leri gizleyen `.local` (mDNS) uzantılarını çözmek için WebRTC üzerinden yerel ağdaki gizli IP'lere **WebSockets** veya **Fetch API** ile (zaman tabanlı yan kanal saldırısı - _Timing Side-Channel Attack_) ping atarak canlı IP'leri tespit eden modern bypass tekniklerini projeye teorik veya pratik olarak ekleyebilirsiniz.

### 4. Kod Temizliği ve Modernize Etme (Promises)

`webrtc_zafiyeti.html` içindeki eski tip `noop` callback yapılarını temizleyip modern `async/await` mimarisine geçirin. Bu, kodun okunabilirliğini ve tarayıcılar arası senkronizasyon başarısını artıracaktır.
