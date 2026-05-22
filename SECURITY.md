# Güvenlik Politikası (Security Policy)

Bu proje (Advanced WebRTC Reconnaissance Module), akademik araştırma ve siber güvenlik eğitimleri kapsamında geliştirilmiş bir Konsept İspatı (Proof of Concept - PoC) çalışmasıdır. Geliştirici olarak, bilgi güvenliği standartlarına ve sorumlu ifşa (responsible disclosure) prensiplerine en yüksek önemi vermekteyiz.

## Desteklenen Sürümler (Supported Versions)

Bu proje eğitim odaklı olduğu için yalnızca en güncel ana sürüm için aktif güvenlik yaması ve hata düzeltme desteği sunulmaktadır.

| Sürüm (Version) | Destek Durumu (Supported) |
| :--- | :--- |
| v2.0.x | ✅ Tam Destek (Aktif) |
| v1.0.x | ❌ Desteklenmiyor (Deprecated) |

## Kapsam (Scope)

Aşağıdaki durumlar bu projenin güvenlik politikası **kapsamındadır**:
* Araç çalışırken kodu barındıran sisteme zarar verebilecek (RCE, XSS vb.) istemci taraflı zafiyetler.
* Araç tarafından yanlış veya yanıltıcı IP tespiti yapılmasına yol açan mantıksal hatalar.
* Savunma mekanizmalarını (mDNS) aşmak için bulunmuş yeni bypass yöntemleri (Eğitim modülüne eklenmek üzere).

Aşağıdaki durumlar **kapsam dışıdır**:
* Tarayıcıların kendi çekirdek (core) WebRTC motorlarındaki sıfırıncı gün (0-day) açıkları (Bu durumlar doğrudan tarayıcı geliştiricilerine bildirilmelidir).
* Sosyal mühendislik tabanlı saldırı senaryoları.

## Zafiyet Bildirimi (Reporting a Vulnerability)

Bu repodaki kodlarda veya modülün çalışma mantığında bir güvenlik zafiyeti tespit ederseniz,
