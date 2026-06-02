# 🔬 CVE-2026-3312: WebKit WebCore Use-After-Free

**Apple WebKit Motorundaki Use-After-Free Zafiyetinin Kapsamlı Analizi ve Rust ile Simülasyonu** **Üniversite Final Ödevi — Siber Güvenlik Araştırma Projesi** [🌐 Canlı Simülasyonu Tarayıcıda Deneyimleyin](https://Pireburak.github.io/Finalproject_MacOS/) *(Pages aktifse bu link çalışacaktır)*

---

## 📖 Proje Hakkında

Bu repository, Apple WebKit medya ve DOM işleme motorunda (WebCore) tespit edilen kritik bir Use-After-Free (UAF) zafiyeti olan **CVE-2026-3312**'nin derinlemesine teknik analizini, saldırı mekanizmasının simülasyonunu ve çözüm önerilerini içermektedir.

Zafiyetin temel sebebi, WebKit'in asenkron DOM timer mekanizmasında (örneğin `setTimeout` callback'leri), DOM elementlerinin worker thread'ler veya arka plan işlemleri hâlâ çalışırken hafızadan serbest bırakılmasıdır. Bu durum klasik bir Use-After-Free race condition'a yol açmakta ve teorik olarak iOS/macOS cihazlarda Uzaktan Kod Çalıştırma (RCE) imkânı sunmaktadır.

Proje; **Rust** ile yazılmış güvenli bir UAF simülasyonu, kapsamlı teknik dokümantasyon, GitHub Actions CI boru hattı otomasyonu ve tarayıcı tabanlı interaktif bir görselleştirme içermektedir.

---

## 📂 Depo Yapısı

```text
Finalproject_MacOS/
│
├── 📁 .github/                     # GitHub topluluk ve CI/CD iş akışları
│   ├── 📁 workflows/
│   │   ├── 📄 rust.yml             # Rust CI — Derleme, test ve lint pipeline
│   │   └── 📄 pages.yml            # GitHub Pages otomatik yayınlama
│   └── 📄 SECURITY.md              # Güvenlik politikası
│
├── 📁 assets/                      # Logo ve görsel dosyalar
│   └── 🖼️ isu-logo.png             # İstinye Üniversitesi logosu
│
├── 📁 docs/                        # Teknik dokümantasyon
│   ├── 📄 zafiyet-analizi.md       # Zafiyet analizi ve CVSS skorlaması
│   ├── 📄 mimari-analiz.md         # WebKit WebCore mimari şeması
│   └── 📄 cozum-onerileri.md       # Çözüm önerileri ve C++ yamaları
│
├── 📁 research_results/            # Ödev araştırma sonuçları
│   ├── 📄 Cevaplarım.md            # İleri düzey soruların cevapları
│   └── 📄 SORULAR.md               # Ödev soruları
│
├── 📁 poc_python/                  # Python analiz araçları
│   └── 📄 exploit.py               # Zafiyet test scripti
│
├── 📁 poc_rust/                    # Rust UAF simülasyonu (Ana PoC)
│   ├── 📁 src/
│   │   └── 📄 main.rs              # Unsafe Rust ile UAF simülasyon mantığı
│   └── 📄 Cargo.toml
│
├── 🌐 simulation.html              # İnteraktif web simülasyon paneli
├── 📄 README.md                    # Bu dosya
└── ⚖️  LICENSE                      # MIT Lisansı
🧠 Zafiyet ÖzetiÖzellikDetayCVE NumarasıCVE-2026-3312Zafiyet TürüUse-After-Free (CWE-416)Etkilenen BileşenApple WebKit (WebCore DOM Engine)CVSS v3.1 Skoru8.8 (High)Saldırı VektörüAğ / Web (Zararlı HTML/JS sayfası)EtkiUzaktan Kod Çalıştırma (RCE) potansiyeliKeşif Tarihi18 Mart 2026Yama Tarihi25 Mart 2026Zafiyetin ÖzüPlaintext[Ana Thread]    setTimeout() çağrılır → Asenkron işlem başlatılır
                      ↓
                DOM Node Silinir → Bellek SERBEST BIRAKILIR ⚠️
                      ↓
[Timer İşlemi]  Serbest bırakılan node bellek adresine erişmeye devam eder → UAF 💥
🚀 Hızlı BaşlangıçGereksinimlerRust 1.70 veya üzeri → rustup.rsPython 3.8 veya üzeriModern bir web tarayıcısı (Safari, Chrome, Firefox)1. Rust PoC — UAF SimülasyonuBash# Projeyi klonlayın
git clone [https://github.com/Pireburak/Finalproject_MacOS.git](https://github.com/Pireburak/Finalproject_MacOS.git)
cd Finalproject_MacOS/poc_rust

# Release modunda derleyin
cargo build --release
🔴 Zafiyetli Senaryo (Race Condition & UAF Gösterimi)Bash# macOS / Linux
./target/release/cve_2026_3312_uaf_poc --mode vulnerable --verbose
Beklenen Çıktı:Plaintext🔬 CVE-2026-3312: WebKit DOM UAF PoC
Mode: vulnerable

⚠️  Running vulnerable scenario...
DOM Node allocated in Arc<Mutex<T>>
🧵 Starting background DOM timer...
🗑️  Main thread destroying DOM Node (UAF trigger)...
Memory corrupted to simulate WebKit UAF
🔄 Timer callback accessing DOM Node...
🚨 UAF detected! Magic number corrupted: 0xFEEDFACE
💥 UAF vulnerability triggered in JavaScript context!
🟢 Yamalanmış Senaryo (Güvenli Senkronizasyon)Bash# macOS / Linux
./target/release/cve_2026_3312_uaf_poc --mode patched --verbose
2. İnteraktif Web SimülasyonuYerel olarak çalıştırmak isterseniz proje kök dizininde aşağıdaki komutu çalıştırıp tarayıcınızdan görüntüleyebilirsiniz:Bashpython3 -m http.server 8000
# Tarayıcınızda açın: http://localhost:8000/simulation.html
🔬 Teknik DetaylarZafiyetli Kod Paterni (C++)C++class DOMTimer {
    void processTimerAsync() {
        worker_thread_ = std::thread([this]() {
            dom_node_->executeCallback(); // Background timer çalışıyor
        });
        // ❌ join() yok — race condition!
    }

    void contextDestroyed() {
        delete dom_node_; // ❌ DOM node hafızadan siliniyor ama timer hala çalışıyor
        dom_node_ = nullptr;
    }
};
Yamalı Kod Paterni (C++)C++class DOMTimer {
    void contextDestroyed() {
        shutdown_requested_ = true;
        worker_cv_.notify_all();

        if (worker_thread_.joinable()) {
            worker_thread_.join(); // ✅ Timer callback tamamlanana kadar bekle
        }

        delete dom_node_; // ✅ Güvenli DOM temizliği
    }
};
Rust Simülasyonu — UAF TespitiRustunsafe fn process_callback(&mut self) -> bool {
    // Magic number bozulduysa WebKit'te UAF gerçekleşmiş demektir
    if self.magic != 0xDEADBEEF {
        println!("🚨 UAF tespit edildi! Magic: 0x{:08X}", self.magic);
        return false;
    }
    self.execution_counter += 1;
    true
}
🛡️ Savunma StratejileriYöntemAçıklamaEtkinlikGarbage Collection (GC)JSCore GC motorunun referansları doğru takip etmesi⭐⭐⭐⭐⭐Smart PointersRefPtr veya WTF::String ile yaşam süresi kontrolü⭐⭐⭐⭐⭐RAII PatternWebCore Objeleri için güvenli destructor yapıları⭐⭐⭐⭐AddressSanitizerGeliştirme sürecinde bellek bozulmalarının tespiti⭐⭐⭐⭐⚠️ Yasal UyarıBu proje yalnızca eğitim ve akademik araştırma amacıyla geliştirilmiştir. Rust simülasyonu, zafiyetin mekanizmasını göstermek için tasarlanmış olup gerçek bir exploit değildir. Buradaki bilgilerin ve araçların yetkisiz sistemler üzerinde kullanılması yasal sorumluluk doğurabilir. Geliştirici hiçbir sorumluluk kabul etmez.📄 LisansBu proje MIT Lisansı ile lisanslanmıştır. Detaylar için LICENSE dosyasına bakınız.👤 Geliştirici Proje Künyesi👤 Adı Soyadı: Burak Özdemir🔢 Öğrenci Numarası: 2520191014🏛️ Bölüm: Bilişim Güvenliği Teknolojisi🎓 Kurum: İstinye Üniversitesi📚 Ders / Kapsam: BGT006 — Sızma Testi Final Ödevi
