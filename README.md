# 📂 Universite Kütüphane Işlemleri gRPC API

Bu proje, bir üniversitenin çevrim içi kütüphane sistemi için geliştirilmiş bir gRPC sunucu ve istemci uygulamasıdır.
Protocol Buffers (protobuf) ile tanımlanan API yapısı üzerinden çalışır.

---

## 🎓 Konular / Servisler

* BookService (Kitaplar)
* StudentService (Öğrenciler)
* LoanService (Ödünçler)

---

## ⚙️ Geliştirme Araçları

* Python 3.12
* grpcio
* grpcio-tools
* Protocol Buffers

---

## ⚡ Kurulum

```bash
git clone https://github.com/mertbaytas/demo-grpc.git
cd demo-grpc
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Proto derleme:

```bash
python -m grpc_tools.protoc -I. --python_out=./src --grpc_python_out=./src university.proto
```

---

## 🚀 Çalıştırma

### Sunucuyu başlatma:

```bash
python src/server/server.py
```

### İstemciyi çalıştırma:

```bash
python src/client/client.py
```

---

## 👀 grpcurl Testleri

Detaylı grpcurl testleri ve ekran görüntüleri için [grpcurl-tests.md](./grpcurl-tests.md) dosyasına bakın.

---

## 🧪 Kullanılan Fonksiyonlar

### BookService

* `ListBooks()`: Tüm kitapları getirir
* `GetBook(id)`: ID ile kitabı getirir
* `CreateBook(book)`: Yeni kitap oluşturur
* `UpdateBook(book)`: Kitabı günceller ✅
* `DeleteBook(id)`: Kitabı siler ✅

### StudentService

* `ListStudents()`: Tüm öğrencileri getirir
* `GetStudent(id)`: ID ile öğrenciyi getirir
* `CreateStudent(student)`: Yeni öğrenci oluşturur
* `UpdateStudent(student)`: Öğrenciyi günceller ✅
* `DeleteStudent(id)`: Öğrenciyi siler ✅

### LoanService

* `ListLoans()`: Tüm ödünç işlemleri
* `GetLoan(id)`: Tekil işlem
* `CreateLoan(studentId, bookId)`: Yeni işlem
* `ReturnLoan(loanId)`: İade işlemi (güncelleme işlevi görür)

> `LoanService` için silme/güncelleme gereksizdir, çünkü iade edilince statü güncellenir.

---

## 📷 Ekran Görselleri

`grpcurl-tests.md` içinde ilgili test çıktılarının ekran görüntüleri `screenshots/` klasörüne konulmalıdır.


Markdown'da referanslama örneği:

```md
![Kitap Listeleme](screenshots/list_books.png)
```

---

## 📦 Proje Yapısı

```
/
├── university.proto
├── README.md
├── grpcurl-tests.md
├── DELIVERY.md
├── requirements.txt
├── screenshots/
│   └── *.png
└── src/
    ├── server/
    │   └── server.py
    └── client/
        └── client.py
```

---

