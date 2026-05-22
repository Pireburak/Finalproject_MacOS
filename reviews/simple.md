## Bilgisayar Dünyasına Yeni Girenler İçin WebRTC IP Sızdırma Zafiyeti – 50 Küçük Adımda Tam Kapsamlı Anlatım

Aşağıdaki adımları sırayla takip ettiğinde, hiçbir teknik ön bilgiye ihtiyaç duymadan bu zafiyetin ne olduğunu, nerede çalıştığını, nasıl korunacağını ve her şeyi öğreneceksin. Her adım bir öncekinin üzerine inşa edilir.

---

### 🔹 TEMEL KAVRAMLAR (1-10)

1. **Bilgisayarın bir adresi vardır:** Tıpkı evinin posta adresin gibi, internete bağlı her cihazın da bir numarası vardır. Buna **IP adresi** denir.

2. **İki tür IP adresi vardır:** **Yerel (Local)** IP – sadece evindeki ağda geçerlidir (örn. 192.168.1.10). **Genel (Public)** IP – tüm internette seni tanıtan adrestir.

3. **Web sitesi normalde IP adresini göremez:** Güvenlik nedeniyle tarayıcılar, bir web sitesinin senin IP adresini almasını engeller. Site sadece “yaklaşık konum” bilir.

4. **WebRTC nedir?** “Web Real-Time Communication” – tarayıcıların kamera/mikrofon kullanmadan, doğrudan birbirine görüntülü konuşabilmesini sağlayan bir teknolojidir (Zoom, Google Meet gibi).

5. **WebRTC’nin bir özelliği vardır:** En hızlı bağlantıyı bulmak için cihazının gerçek IP adreslerini öğrenmesi gerekir. Bu normalde iyidir, çünkü görüşme kalitesini artırır.

6. **Kötü niyetli bir web sitesi bu özelliği kötüye kullanabilir:** Sadece senin haberin olmadan arka planda WebRTC’yi başlatır ve IP adreslerini alır.

7. **Buna “WebRTC IP Sızdırma Zafiyeti” denir:** Aslında WebRTC’nin kendisi hatalı değil; sitelerin bu bilgiyi izinsiz toplaması bir **gizlilik zafiyetidir**.

8. **Bu zafiyet her yerde çalışır:** Telefonda (Android, iOS), tablette, bilgisayarda (Windows, Mac, Linux), hatta internete bağlı bir arabada bile.

9. **Tarayıcı yeterlidir:** Chrome, Firefox, Safari, Edge, Opera… WebRTC’yi destekleyen her tarayıcı bu zafiyete açıktır (koruma ayarları değişebilir).

10. **Ne yüklemen gerekmez:** Siteye tıklaman yeterli. Özel bir izin vermene, eklenti kurmana gerek yoktur.

---

### 🔹 BU ZAFİYET NASIL ÇALIŞIR? (11-20)

11. **Bir web sitesi seni ziyaret ettiğinde** arka planda JavaScript kodu çalıştırır. Bu kod çok kısadır, 10 satır bile olabilir.

12. **Kod, sahte bir “görüşme odası” açar:** `RTCPeerConnection` adlı bir nesne oluşturur. Bu, WebRTC’nin kalbidir.

13. **İçinde boş bir “data kanalı” oluşturur:** `createDataChannel("")` – bu kanal aslında hiçbir şey göndermez, sadece IP adreslerini toplamaya yarar.

14. **Bir “teklif” (offer) hazırlar:** `createOffer()` komutu, tarayıcıya “Şu an bir görüşme başlatmak istiyorum, bana ağ bilgilerimi ver” der.

15. **Tarayıcı bir SDP paketi üretir:** SDP = “Session Description Protocol”. Bu paket, cihazın tüm ağ arayüzlerini (Wi-Fi, ethernet, VPN) listeler.

16. **SDP’nin içinde “candidate” satırları vardır:** Her candidate, bir IP adresi + port numarası içerir. Bu adresler yerel IP’dir.

17. **Ayrıca STUN sunucusuna sorar:** STUN = “Session Traversal Utilities for NAT”. Harici bir sunucuya (örneğin Google’ın stun.l.google.com) “Beni dışarıdan nasıl görüyorsun?” diye sorar.

18. **STUN sunucusu gerçek genel IP’ni döndürür:** İşte bu, VPN kapalı olsa bile gerçek kimliğindir.

19. **Kod, tüm bu candidate satırlarını tarar:** Basit bir desen (regex) kullanarak IP’ye benzeyen sayıları bulur (`192.168.1.5` gibi).

20. **Bulduğu IP’leri ekrana yazar veya kendi sunucusuna gönderir:** Saldırgan böylece hem yerel hem genel IP’ni ele geçirir.

---

### 🔹 BU GERÇEKTEN BİR ZAFİYET Mİ? (21-25)

21. **Evet, resmen “Gizlilik Zafiyeti” olarak kabul edilir:** Dünyadaki tüm büyük tarayıcı şirketleri (Google, Mozilla, Apple) bu konuyu ciddiye alır.

22. **Her yıl yeni araştırmalar yayınlanır:** 2025 ve 2026’da bile bu zafiyetin yeni varyasyonları keşfedilmiştir.

23. **CVE numarası vardır:** Örneğin **CVE-2026-6752** – Firefox’un WebRTC bileşeninde bulunan bir sınır hatası.

24. **Ancak bu, klasik bir “yazılım hatası” değildir:** WebRTC’nin tasarımından gelir. Bu yüzden tamamen “düzeltilmiş” bir sürüm yoktur; sadece risk azaltılır.

25. **Yani güncel tarayıcıda bile çalışabilir:** Koruma ayarları açık olsa dahi, genel IP’ni sızdırmak mümkündür.

---

### 🔹 HANGİ BİLGİLER ELE GEÇİRİLEBİLİR? (26-30)

26. **Gerçek genel IP adresin:** İnternet servis sağlayıcının (Turkcell, Vodafone, TTNet vb.) sana verdiği adres. Bu adresle şehrin, hatta semtin kabaca bulunabilir.

27. **Yerel IP adresin:** Ev ağındaki numaran (192.168.x.x). Bununla saldırgan, evindeki ağın yapısını anlayabilir.

28. **Tarayıcı parmak izi (fingerprint):** User-Agent string’i sayesinde hangi işletim sistemini, hangi tarayıcı sürümünü kullandığın öğrenilir.

29. **Bu bilgilerle ne yapılabilir?** Hedefli reklam, DDoS saldırısı (internetini çökertme), veya seni takip etme.

30. **VPN kullanıyor olsan bile bu bilgiler sızar:** Çünkü WebRTC, VPN tünelini atlayarak doğrudan ağ kartına sorar.

---

### 🔹 NASIL KORUNURUZ? (31-40)

31. **VPN tek başına işe yaramaz!** Hatta yanlış güvenlik hissi yaratır. WebRTC, VPN’i görmezden gelir.

32. **En etkili yöntem: Tarayıcı eklentisi** – “WebRTC Leak Prevent” veya “WebRTC Protect” yükle.

33. **Bu eklentiler ne yapar?** WebRTC’nin tüm trafiğini bir proxy üzerinden yönlendirmeye zorlar, böylece gerçek IP gizlenir.

34. **Alternatif: Tarayıcının gizli ayarları** – Chrome’da `chrome://flags` yaz, “Anonymize local IPs” seçeneğini “Enabled” yap.

35. **Firefox’ta:** `about:config` yaz, `media.peerconnection.ice.obfuscate_host_addresses` değerini `true` yap.

36. **En radikal çözüm:** WebRTC’yi tamamen devre dışı bırakan eklenti kullan. Ancak o zaman Google Meet, Discord gibi uygulamalar çalışmaz.

37. **Safari (macOS/iOS):** Varsayılan olarak mDNS koruması aktiftir. Yerel IP yerine rastgele bir `xxxx.local` adresi gösterir. Yine de genel IP korunmaz.

38. **Hiçbir yöntem %100 değildir:** Güncel araştırmalar, eklentilerin bile bazen aşılabildiğini göstermektedir.

39. **Konteyner (Docker) ile çalıştırmak:** Tüm tarayıcı trafiğini bir sanal katmana hapsedip VPN üzerinden yönlendirmek en güvenlisidir, ama karmaşıktır.

40. **Test etmek için:** Bu projedeki HTML dosyalarını aç, IP’lerini gör. Eklentiyi kurduktan sonra tekrar dene – farkı anlarsın.

---

### 🔹 UZAKTAN MI, YAKINDAN MI? AYAK İZİ BIRAKIR MI? (41-45)

41. **Tamamen uzaktan sömürülür:** Saldırganın yanında olması gerekmez. Sadece seni kendi sitesine çekmesi yeterlidir.

42. **Herhangi bir site bu kodu işletebilir:** Bir haber sitesine bile reklam yoluyla bu kod yerleştirilebilir.

43. **Saldırı iz bırakır mı?** Senin bilgisayarında neredeyse hiç iz kalmaz. Sadece normal bir web sitesi ziyareti gibi görünür.

44. **Ağda iz bırakabilir:** Kurumsal bir güvenlik duvarı, STUN sorgularını tespit edebilir. Ev ağında ise genellikle fark edilmez.

45. **Saldırganın sunucusunda kayıt kalır:** Eğer saldırgan gelen IP’leri loglarsa, bu bir iz olur. Ama senin bilgisayarında silinmez bir dosya oluşmaz.

---

### 🔹 PROJE DOSYALARINDAKİ ÖNEMLİ NOTLAR (46-50)

46. **`webrtc_zafiyeti.html`:** Sadece yerel IP’leri gösterir (STUN sunucusu kullanmaz). Modern tarayıcılarda mDNS koruması varsa `.local` adresleri görürsün.

47. **`webrtc_zafiyeti2.html`:** Google’ın STUN sunucusunu kullanır. Hem yerel hem genel IP’ni gösterir. Ayrıca ham SDP paketini ekrana basar.

48. **`README.md`** çok iyi hazırlanmış, ancak ekran görüntüsü yer tutucusu kalmış. Ayrıca mDNS korumasını anlatır.

49. **`SECURITY.md`** tamamlanmamış – iletişim adresi yok. Bu, sorumlu ifşa için eksikliktir.

50. **Sonuç:** Bu PoC, eğitim için harika bir araçtır. Ancak üretim ortamında kullanılmadan önce IPv6 desteği, regex iyileştirmeleri ve asenkron hata düzeltmeleri yapılmalıdır.

---

### ⚡ HIZLI ÖZET (Cevap Niteliğinde)

- **Nerede çalışır?** Tarayıcıda (Chrome, Firefox, Safari vb.) – her cihazda.
- **Bir zafiyet mi?** Evet, gizlilik zafiyeti.
- **Nerede bulunur?** Telefon, laptop, tablet, araba (eğer WebRTC destekliyorsa).
- **Hangi versiyonlarda?** WebRTC’nin olduğu tüm sürümlerde. Tam düzeltme yok.
- **Nasıl korunuruz?** VPN işe yaramaz. WebRTC engelleyici eklenti veya tarayıcı ayarları şart.
- **Ne bilgiler gider?** Gerçek IP (yerel+genel), tarayıcı parmak izi.
- **Uzaktan mı?** Evet, tek tıklamayla.
- **Ayak izi?** Cihazında yok, ağda var (tespit edilebilir).
