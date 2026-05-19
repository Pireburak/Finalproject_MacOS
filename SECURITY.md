# Güvenlik Politikası (Security Policy)

Bu projede güvenli kodlama standartlarına ve veri gizliliğine büyük önem verilmektedir. Lütfen tespit ettiğiniz güvenlik zafiyetlerini açık bir "Issue" oluşturmak yerine aşağıda belirtilen kanallar üzerinden bildiriniz.

## Desteklenen Sürümler

Aşağıdaki proje sürümleri şu anda güvenlik güncellemeleri almaktadır:

| Sürüm | Güvenlik Desteği |
| :--- | :--- |
| v1.0.x | ✅ Aktif Destekleniyor |
| < 1.0 | ❌ Desteklenmiyor |

## Zafiyet Bildirim Süreci

Eğer bu projede bir güvenlik açığı tespit ederseniz, durumu bildirmek için lütfen aşağıdaki adımları izleyin:

1. Tespit ettiğiniz açığı (PoC - Proof of Concept) detaylandıran bir rapor hazırlayın. Raporda zafiyetin nerede olduğu ve nasıl tetiklendiği açıkça belirtilmelidir.
2. Bu raporu doğrudan `[Senin E-posta Adresin]` adresine "GÜVENLİK ZAFİYETİ BİLDİRİMİ" başlığı ile gönderin.
3. Gelen bildirimler en geç 48 saat içerisinde değerlendirilecek, doğrulama yapıldıktan sonra gerekli yama yayınlanana kadar süreç gizli tutulacaktır.

## Projede Uygulanan Güvenlik Prensipleri

Uygulamanın mimarisinde aşağıdaki temel güvenlik standartları göz önünde bulundurulmuştur:

* **En Az Yetki Prensibi (Least Privilege):** macOS ortamında uygulamanın çalışması için yalnızca zorunlu sistem izinleri talep edilmiştir.
* **Girdi Doğrulama (Input Validation):** Uygulama içerisindeki veri giriş noktaları, manipülasyon ve enjeksiyon risklerine karşı kontrol edilmektedir.
* **Güvenli Veri Saklama:** Hassas veriler düz metin (plaintext) formatında tutulmaz, işletim sisteminin güvenli depolama mekanizmaları tercih edilir.
* git add SECURITY.md
git commit -m "Güvenlik politikası (SECURITY.md) eklendi"
git push origin main
