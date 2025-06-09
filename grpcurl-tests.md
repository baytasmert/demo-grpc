### 📘 BookService Testleri

# 🔍 Tüm kitapları listele
grpcurl -plaintext -d '{}' localhost:50051 university.BookService/ListBooks

![alt text](screenshots/ListBooks.png)

# ➕ Yeni kitap ekle (örnek UUID)
grpcurl -plaintext -d '{
  "book": {
    "id": "11111111-1111-1111-1111-111111111111",
    "title": "Test Book",
    "author": "Test Author",
    "isbn": "1234567890123",
    "publisher": "Test Pub",
    "pageCount": 100,
    "stock": 2
  }
}' localhost:50051 university.BookService/CreateBook

![alt text](screenshots/CreateBook.png)

# ✏️ Kitap güncelle (aynı ID ile)
grpcurl -plaintext -d '{
  "book": {
    "id": "11111111-1111-1111-1111-111111111111",
    "title": "Test Book Updated",
    "author": "New Author",
    "isbn": "1234567890123",
    "publisher": "New Pub",
    "pageCount": 120,
    "stock": 5
  }
}' localhost:50051 university.BookService/UpdateBook

![alt text](screenshots/UpdateBook.png)

# ❌ Kitap sil
grpcurl -plaintext -d '{"id": "11111111-1111-1111-1111-111111111111"}' localhost:50051 university.BookService/DeleteBook

![alt text](screenshots/DeleteBook.png)

### 👤 StudentService Testleri

# 🔍 Tüm öğrencileri listele
grpcurl -plaintext -d '{}' localhost:50051 university.StudentService/ListStudents

![alt text](screenshots/ListStudents.png)

# ➕ Yeni öğrenci ekle
grpcurl -plaintext -d '{
  "student": {
    "id": "22222222-2222-2222-2222-222222222222",
    "name": "Test Student",
    "studentNumber": "999999",
    "email": "test@student.com",
    "isActive": true
  }
}' localhost:50051 university.StudentService/CreateStudent

![alt text](screenshots/CreateStudent.png)

# ✏️ Öğrenci güncelle
grpcurl -plaintext -d '{
  "student": {
    "id": "22222222-2222-2222-2222-222222222222",
    "name": "Updated Student",
    "studentNumber": "999999",
    "email": "updated@student.com",
    "isActive": true
  }
}' localhost:50051 university.StudentService/UpdateStudent

![alt text](screenshots/UpdateStudent.png)

# ❌ Öğrenci sil
grpcurl -plaintext -d '{"id": "22222222-2222-2222-2222-222222222222"}' localhost:50051 university.StudentService/DeleteStudent

![alt text](screenshots/DeleteStudent.png)

### 🔄 LoanService Testleri

# 🔁 Loan oluştur
grpcurl -plaintext -d '{
  "studentId": "EXISTING_STUDENT_ID",
  "bookId": "EXISTING_BOOK_ID"
}' localhost:50051 university.LoanService/CreateLoan

![alt text](screenshots/CreateLoan.png)

# 📄 Loan iade et
grpcurl -plaintext -d '{"loanId": "EXISTING_LOAN_ID"}' localhost:50051 university.LoanService/ReturnLoan

![alt text](screenshots/ReturnLoan.png)