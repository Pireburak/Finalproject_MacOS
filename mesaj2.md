Merhaba,

Şimdi ikinci aşamaya geçelim. Bir polis dedektifi gibi düşün — suçluyu yakalamak için:

1. **Nerede durman lazım?** (Gözlem Noktası)
   - Ağ trafiğinin geçtiği bir noktada olmalısın: bilgisayarın ağ kartında (localhost), modem/gateway'de, ya da bir sunucunun önünde
   - Tıpkı bir polisin suçluyu görmek için sokak köşesinde beklemesi gibi, sen de `Wireshark`, `tcpdump` veya `netstat` gibi araçlarla ağın "köşesinde" beklersin
   - Dinlediğin yer yanlışsa, suçluyu kaçırırsın

2. **Neleri çevirmen (analiz etmen) lazım?** (Deşifre)
   - **Ham veriyi oku:** Gelen giden paketler ham byte'lar halindedir. Bunları insan okuyabilir hale getirmelisin (hex → ASCII, binary → metin)
   - **Port numaralarını çevir:** 22 = SSH, 80 = HTTP, 443 = HTTPS, 445 = SMB... Hangi kapıdan giriyor?
   - **IP adreslerini çöz:** Bu IP kime ait? Yerel mi? Genel mi? Hangi ülkeden? VPN mi?
   - **Protokolü tanı:** TCP mi UDP mi? ICMP mi? Ne tür bir bağlantı kurulmaya çalışılıyor?
   - **Zaman damgalarını bağla:** Bu trafik saat 03:00'te mi geliyor? Bu normal mi?

3. **Çevirince neyi inceleyeceksin ki suçlu olduğunu anlayasın?** (Tespit)
   - **Anormallik ara:** Normalde hiç gitmediğin bir IP'ye bilgisayarın sürekli paket mi gönderiyor? Bu şüpheli.
   - **Tarama desenleri:** Aynı IP'den saniyeler içinde yüzlerce farklı porta bağlantı geliyorsa — bu bir port taramasıdır (recon). Saldırgan "kapı yokluyor" demektir.
   - **Banner toplama:** Birisi gelip 22, 80, 443 portlarına sırayla bağlanıp "Kimsin?" diye soruyorsa — bu banner grabbing'dir. Keşif yapıyor.
   - **Bilinen imzalar (signature):** Giden paketlerin içinde "etc/passwd", "admin", "SELECT * FROM" gibi kelimeler var mı? Bunlar saldırı desenleridir.
   - **Davranışsal analiz:** Normalde 5 dakikada 10 bağlantı yaparken, şimdi 1 dakikada 200 bağlantı mı var? Trafik fırtınası — bu DDoS veya tarama olabilir.

4. **Polis mantığıyla özet:**
   - **Olay yeri:** Ağ trafiğinin geçtiği nokta (network interface)
   - **Delil:** Gelen/giden paketler (raw packets)
   - **Tercüman:** Wireshark, tcpdump, snort gibi araçlar (çeviriyi senin için yapar)
   - **Kanıt:** Anormal desenler, taramalar, bilinen saldırı imzaları, zaman dışı trafik
   - **Tutuklama:** Tespit ettiğin anomaliyi raporla, kaynağını engelle (firewall kuralı)

Yani kod yazmadan önce konuyu anlamak neyse, ağ güvenliğinde de elindeki ham veriyi anlamak odur. Önce çevir, sonra analiz et, sonra karar ver.

Kolay gelsin!
