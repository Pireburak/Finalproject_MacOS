WebRTC IP Sızdırma Zafiyeti hakkındaki sorularınızı aşağıda tüm detaylarıyla yanıtlamaya çalışacağım.

### 1. Bu Zafiyet Nerede Çalışır?

Bu zafiyet, doğrudan işletim sisteminizde veya donanımınızda değil, **WebRTC özelliğini destekleyen tüm modern web tarayıcılarında** çalışır. WebRTC, Chrome, Firefox, Safari, Edge, Opera, Brave gibi tarayıcılara varsayılan olarak entegre edilmiş bir teknolojidir. Yani bir web sitesini ziyaret ettiğinizde, site sizin haberiniz olmadan arka planda çalışan küçük bir JavaScript kodu ile bu zafiyeti tetikleyebilir. **WebRTC'nin kendisi bir "bug" değil, bir özelliktir; fakat bir web sitesi tarafından istenmeyen bir şekilde kullanılması bir gizlilik zafiyeti oluşturur**. Bu nedenle, zafiyetin oluşması için ekstra bir yazılım yüklemenize veya herhangi bir izin vermenize gerek yoktur.

### 2. Bu Bir Zafiyet mi?

Evet, **WebRTC IP Sızdırma (Leak) zafiyeti, "Privacy Vulnerability" yani "Gizlilik Zafiyeti" kategorisine girer**. Sadece bir teoriden ibaret değildir, güncel sistemler üzerinde yapılan bilimsel çalışmalarla varlığı kanıtlanmış gerçek bir risktir. Bu konuda 2025 ve 2026 yıllarında yayınlanmış birçok güncel akademik çalışma ve rapor bulunmaktadır. Örneğin:

- 2025 yılında yayınlanan bir araştırma, WebRTC'nin mDNS gibi güncel koruma yöntemlerinin sınırlarını aşarak IP adreslerini nasıl sızdırabildiğini göstermiştir.
- 2026 yılı itibarıyla, birçok büyük tarayıcıda hala bu zafiyetin mevcut olduğuna dair güncel rehberler ve makaleler bulunmaktadır.

### 3. Zafiyet Hangi Cihazlarda Bulunur? (Telefon, Laptop, Tablet, Araba?)

Bu zafiyet, **WebRTC'yi destekleyen bir tarayıcıya sahip olan tüm cihazları** potansiyel olarak etkiler. Bu cihazlar:

- **Masaüstü ve Dizüstü Bilgisayarlar (Windows, macOS, Linux):** En yaygın risk grubudur. En güncel işletim sistemlerinde ve tarayıcılarda bile bu zafiyet tespit edilebilmektedir.
- **Akıllı Telefonlar ve Tabletler (Android, iOS):** Bu cihazlarda da zafiyet mevcuttur. Örneğin, bir araştırmada Android cihazlarda Chrome ve Firefox tarayıcılarının yerel ağ adreslerini sızdırdığı gözlemlenmiştir. Safari'nin koruma yöntemleri farklı olsa da, iOS cihazlar da bu konuda tamamen güvenli değildir.
- **Araba ve Diğer IoT Cihazları:** Bir aracın veya buzdolabının internet tarayıcısı varsa ve bu tarayıcı WebRTC'yi destekliyorsa, teorik olarak bu cihazlar da bu zafiyetten etkilenebilir. Ancak pratikte en büyük risk grubunu kişisel bilgisayarlar ve akıllı telefonlar oluşturmaktadır.

### 4. Zafiyet Hangi Versiyonlarda Bulunur? (Yamalar ve Düzeltmeler)

Bu kritik bir noktadır: **Bu zafiyet, WebRTC'nin temel tasarımından kaynaklandığı için tamamen "düzeltilmiş" bir sürüm yoktur**. Bu, periyodik olarak yamanan klasik bir yazılım hatası (bug) değildir. Ancak tarayıcı üreticileri riski azaltmak için çeşitli koruma katmanları eklemişlerdir:

- **Güncel Yaklaşım (mDNS Obfuscation):** 2019'dan itibaren Chrome, Edge, Opera gibi tarayıcılar, **mDNS (Multicast DNS)** adı verilen bir teknoloji ile yerel IP adresinizi gizlemeye başlamıştır. Bu yöntem, gerçek IP adresinizi (örn. `192.168.1.10`) rastgele oluşturulmuş ve geçici bir `.local` adresiyle değiştirir. Proje dosyanızdaki `README.md` dosyasında da bu konuya detaylıca değinilmiştir. **Ancak**, bu koruma yöntemi genel (public) IP adresinizi sızdırmayı engelleyemez.
- **Tam Düzeltme Değil, Risk Azaltma:** Tarayıcılar, WebRTC'nin proxy veya VPN üzerinden çalışmasını zorlamak gibi farklı ayarlar sunar (bazıları `about:flags` gibi geliştirici menülerinde gizlidir), ancak bunlar her zaman %100 etkili değildir.
- **Yeni Zafiyetler (CVE'ler):** WebRTC ile ilgili yeni zafiyetler keşfedilmeye devam etmektedir. Örneğin, 2026 yılında yayınlanan **CVE-2026-6752** numaralı zafiyet, Firefox tarayıcısının WebRTC bileşeninde bulunan bir sınır koşulu hatasını (incorrect boundary conditions) tanımlamakta ve bu hatanın belirli sürümlerde (Firefox 150, ESR 115.35, ESR 140.10) yamalandığı belirtilmektedir.

Özetle, **hiçbir güncel tarayıcı bu zafiyete karşı %100 koruma sağlamamaktadır**; sadece risk seviyesi değişmektedir.

### 5. Nasıl Korunuruz? (VPN ve Diğer Yöntemler)

**VPN, tek başına bu zafiyete karşı bir çözüm değildir ve hatta yanlış bir güvenlik hissi yaratabilir.** Maalesef, WebRTC zafiyetinin en bilinen ve tehlikeli özelliği, **aktif bir VPN bağlantınız olsa dahi çalışmasıdır**. Bunun sebebi, WebRTC'nin tarayıcı ayarlarınızı ve VPN'in oluşturduğu tüneli (tunnel) görmezden gelerek, doğrudan sisteminizin ağ arayüzleri üzerinden istek (STUN request) gönderebilmesidir. Bu sayede sizin yerel ve gerçek genel IP adresinizi kolayca ifşa edebilir.

Etkili korunma yöntemleri şunlardır:

1.  **Tarayıcı Eklentileri (En Pratik Çözüm):** WebRTC sızıntılarını engellemek için özel olarak geliştirilmiş tarayıcı eklentilerini kullanabilirsiniz:
    - **WebRTC Leak Prevent**: "Disable non-proxied UDP (force proxy)" modunu seçerek WebRTC'yi yalnızca proxy üzerinden çalışmaya zorlar.
    - **WebRTC Protect**: Bu eklenti, özel IP adresinizi gizleyebilir ve WebRTC trafiğini bir proxy sunucusu üzerinden yönlendirebilir.
2.  **Tarayıcının Geliştirici Ayarları (Kısmi Çözüm):**
    - **Chrome/Edge:** Adres çubuğuna `chrome://flags` yazın, "WebRTC" aratın ve "**Anonymize local IPs exposed by WebRTC**" seçeneğini "**Enabled**" olarak değiştirin. Bu ayar yalnızca yerel IP'nizi gizler.
    - **Firefox:** Adres çubuğuna `about:config` yazın, "`media.peerconnection.ice.obfuscate_host_addresses`" tercihini bulun ve değerini `true` yapın.
3.  **WebRTC'yi Tamamen Devre Dışı Bırakmak (En Radikal Çözüm):** WebRTC'ye ihtiyacınız yoksa, tarayıcınızın eklenti mağazasından bu özelliği tamamen devre dışı bırakan eklentiler bulabilirsiniz. Bu, tüm WebRTC tabanlı uygulamaları (Google Meet, Discord vb.) devre dışı bırakacağı için kullanışsız olabilir.
4.  **Farklı Bir Tarayıcı Kullanmak:** WebRTC özelliğini desteklemeyen tarayıcılar (örneğin, eski sürüm Internet Explorer) bu zafiyetten etkilenmez ancak bu yöntem pratik değildir.
5.  **Container Kullanımı (İleri Seviye):** Bilimsel araştırmalar, Firefox'u Docker gibi bir konteyner (container) içinde çalıştırıp tüm trafiği VPN üzerinden yönlendirmenin bu zafiyeti tamamen engelleyebildiğini göstermiştir.

### 6. Ne Gibi Bilgiler Ele Geçirilebilir?

Bir saldırgan bu zafiyeti kullanarak şu kritik bilgilere ulaşabilir:

- **Gerçek Genel (Public) IP Adresiniz:** Bu, internet servis sağlayıcınız (İSS) tarafından size atanan ve internetteki dijital adresinizdir. Bu adres ile coğrafi konumunuz (şehir, semt) kabaca tespit edilebilir.
- **Yerel (Local) IP Adresiniz ve Ağ Topolojiniz:** Ev veya iş ağınızdaki adresiniz (örneğin, `192.168.1.10`) ele geçirilebilir. Bu, saldırganın sadece sizi değil, içinde bulunduğunuz ağ yapısını da anlamasını sağlar.
- **Cihaz ve Tarayıcı Parmak İzi (Fingerprint):** Bu bilgi, tarayıcı eklentileriniz, işletim sisteminiz, ekran çözünürlüğünüz gibi birçok parametre ile birleştirildiğinde sizi rahatlıkla teşhis etmeye yeter.

Bu bilgilerle bir saldırgan şunları yapabilir:

- Size karşı hedefli bir siber saldırı düzenleyebilir.
- DDoS (Dağıtılmış Hizmet Engelleme) saldırısı ile internet bağlantınızı çevrimdışı bırakabilir.
- Çevrimiçi takip ve reklam hedeflemeyi çok daha etkili hale getirebilir.

### 7. Bu Zafiyet Uzaktan mı, Yoksa Yakından mı Sömürülür?

**Tamamen uzaktan sömürülebilir!** Saldırganın fiziksel olarak size veya cihazınıza yakın olması gerekmez. Tek yapması gereken, sizi ziyaret ettiğiniz bir web sitesine (kendi kontrolündeki bir siteye veya güvenliğini aştığı başka bir siteye) yönlendirmektir. Sitenin arka planında çalışan ufak bir JavaScript kodu, siz daha ne olduğunu anlamadan IP adresinizi alıp saldırgana gönderebilir.

### 8. Bu Zafiyet Bir Ayak İzi (Forensic Artifact) Bırakır mı?

Bu, teknik olarak biraz karmaşık bir sorudur. Saldırının **hedef tarafında** (yani sizin cihazınızda) neredeyse hiçbir iz bırakmaz. Siz sadece sıradan bir web sitesini ziyaret etmiş olursunuz. Tarayıcı kayıtlarına bakılsa dahi, bir WebRTC sorgusunun mu yoksa normal bir video görüşmesi için mi yapıldığını ayırt etmek çok zordur.

Ancak saldırganın **kendi sunucularında** bu sorguların kaydını tutması halinde, bu sorgular dijital bir iz olarak kalacaktır. Fakat kurumsal bir ağda bir güvenlik duvarı veya ağ izleme aracı (NGFW, IDS/IPS gibi) bu tür STUN sorgularını ve anormal WebRTC trafiğini tespit edebilir. Yani, bu zafiyet sizin kişisel cihazınızda bir dosya veya log bırakmaz, ancak ağ trafiği analiz edilerek varlığı tespit edilebilir.

---

Bu açığın bir yazılım hatasından çok, "WebRTC" isimli bir özelliğin kötü niyetli kullanımı olduğunu unutmamak önemlidir. Yukarıda belirttiğim eklentileri kurarak kendinizi bu tehdide karşı etkili bir şekilde koruyabilirsiniz.
