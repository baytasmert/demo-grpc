# gRPC Uygulama Geliştirme Ödevi Teslim Raporu

## 👤 Öğrenci Bilgileri

* **Ad Soyad**: Mert Baytaş
* **Öğrenci Numarası**: 138320067
* **Kullanılan Programlama Dili**: Python

---

Bu proje, üniversitedeki “Açık Kaynak Kodlu Yazılımlar” dersi kapsamında geliştirdiğim bir gRPC uygulamasıdır. Öğrenci, kitap ve ödünç alma işlemlerini yöneten bir sistem oluşturarak hem gRPC protokolünü hem de protobuf tanımlarını uygulamalı olarak kullandım. Öncelikle university.proto adlı dosyada mesaj yapıları, servisler ve metodlar tanımlandı. Enum kullanımı ile ödünç işlemlerinin durumları (ONGOING, RETURNED) belirtildi. Bu .proto dosyasından sunucu ve istemci tarafında kullanılmak üzere stub kodlar grpc_tools.protoc ile üretildi. Python ile yazdığım server.py dosyasında üç ayrı servis (BookService, StudentService, LoanService) in-memory tabanlı veri yapıları ile gerçeklendi. Her servis için gerekli CRUD (oluşturma, listeleme, güncelleme, silme) metodları yazıldı.

İstemci tarafında ise yine Python kullanılarak client.py dosyası geliştirildi ve bu dosya üzerinden tüm servisler test edildi. Ayrıca terminal üzerinden servisleri manuel olarak test edebilmek için grpcurl aracı kuruldu,  çıkan sonuçlar terminalde doğrulandı ve ekran görüntüleri grpcurl-tests.md dosyası ile birlikte sunuldu. grpcurl ile fonksiyonları çağırabilmek için Reflection özelliği server.py koduna eklendi.Sonuç olarak tüm servislerin doğru şekilde çalıştığı, eklenen kitapların güncellenip silinebildiği, öğrencilerin ve ödünç işlemlerinin yönetilebildiği gözlemlendi.

---

## 📦 GitHub Repo

Projenin tamamı GitHub'a yüklenmiştir. `university.proto` dosyasına ait stub dosyalar çıkarılmıştır.

### 🔗 GitHub Repo Linki

[https://github.com/baytasmert/demo-grpc](https://github.com/baytasmert/demo-grpc)

---

## 📄 .proto Dosyası

* `.proto` dosyasının adı: `university.proto`
* Tanımlanan servisler:

  * `BookService` (4 metod)
  * `StudentService` (4 metod)
  * `LoanService` (2 metod)
* Toplam metod sayısı: 10
* Enum kullanımı: `LoanStatus` enum'u `Loan` mesajında kullanılmıştır
* Dildeki tercih: Tüm tanımlar İngilizce, grpcurl-tests dokümanı ve delivery raporu Türkçe

---

## 🧪 grpcurl Test Dokümantasyonu

Tüm `grpcurl` komutları, ekran görüntüleri ve doğrulama senaryoları `grpcurl-tests.md` dosyasında açıklanmıştır.

Dosya içeriği:

* Tüm servisler için doğru istek örnekleri
* Her bir testin ekran görüntüsü `screenshots/` klasörü altına yerleştirilmiştir
* Yanlış ID gönderimi gibi hatalı senaryolar da belgelenmiştir

Dosya: [`grpcurl-tests.md`](https://github.com/baytasmert/demo-grpc/blob/main/grpcurl-tests.md)

---

## 🛠️ Derleme ve Çalıştırma Adımları

```bash
# protobuf stub dosyalarını üretmek için:
python -m grpc_tools.protoc -I=./src/proto --python_out=./src --grpc_python_out=./src ./src/proto/university.proto

# Sunucuyu başlat:
python src/server/server.py

# Ayrı bir terminalde istemciyi çalıştır:
python src/client/client.py
```

---

## ⚠️ Kontrol Listesi

* [x] Stub dosyaları GitHub reposuna eklenmedi
* [x] grpcurl komutları test belgesinde yer alıyor
* [x] Ekran görüntüleri test belgesine eklendi
* [x] Tüm servisler çalışır durumda
* [x] README.md içinde yeterli açıklama var

---


