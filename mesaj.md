Merhaba,

Kod yazmaya başlamadan önce, projeyi küçük parçalara bölmek ve her bir parçanın ne yaptığını anlamak çok önemlidir. Şimdiye kadar ne yaptığımızı düşünelim:

1. **Proje Nedir?** - Bu proje, macOS sistemlerinde network keşfi (recon) ve banner grabbing yapabilen bir araç. Amaç, hedef sistemler hakkında bilgi toplamak ve açıklarını tespit etmek.

2. **Nasıl Çalışır?** - Temel olarak:
   - Hedef IP ve portlara TCP bağlantısı kurar
   - Zararsız paketler göndererek servislerin banner'larını (imzalarını) alır
   - Renkli terminal çıktıları ile kullanıcıya bilgi sunar
   - Socket programlama ve network protokollerini kullanır

3. **Mantığı Anlamak Önemlidir** - Kodun kendisini yazmak sadece syntaxı doğru kullanmak değil, arka plandaki mantığı anlamak demektir. Bu nedenle:
   - Önce mevcut kodu okuyup anlamaya çalış
   - Her fonksiyonun ne yaptığını, girdi/çıktılarını incele
   - Network akışını ve veri hareketlerini takip et
   - Testlerle nasıl çalıştığını gözlemle

4. **Kod Önemli Değil, Anlamak Önemli** - İlk başta hatalar yapmak, kodun tamamını anlamak için gereklidir. Kendine zaman tanı, tekrar tekrar okuyup, debug ederek öğren.

---

### 🧩 Bak nasıl yapmışım — Örnek: `simple.md` ve `infographic.html`

Bu iki dosyaya bakarsan, karmaşık bir konuyu (WebRTC IP Sızdırma Zafiyeti) nasıl küçük parçalara böldüğümü görürsün:

**`simple.md`** — 50 Küçük Adım:
- Konuyu 6 bölüme ayırdım: Temel Kavramlar → Nasıl Çalışır → Zafiyet mi? → Ne bilgiler gider? → Nasıl Korunuruz? → Proje Notları
- Her bölümü 5-10 küçük adıma böldüm
- Her adım bir öncekinin üzerine inşa ediliyor, sırayla gidiyor
- En sonunda hızlı bir özet tablosu koydum

**`infographic.html`** — Görsel Rehber:
- Aynı konuyu bu sefer 8 görsel bölüme ayırdım
- Her bölüm için kartlar, ikonlar ve görsel diyagramlar kullandım
- Renk kodlaması yaptım: kırmızı = tehlike, yeşil = korunma, mavi = kavram
- Karmaşık akışları basit oklarla (1→2→3) görselleştirdim

**İkisinin ortak noktası:** Büyük bir konuyu alıp aklında sıralı, küçük ve anlaşılır parçalara bölmek. Önce her parçayı tek başına anlamak, sonra parçaların birbiriyle nasıl bağlandığını görmek. Kod da tam olarak böyle öğrenilir.

---

Unutma: "Önce anla, sonra kodla" her zaman işe yarar.

Kolay gelsin!
