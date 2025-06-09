# src/client/client.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# client.py
import grpc
import uuid
import university_pb2
import university_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    book_stub = university_pb2_grpc.BookServiceStub(channel)
    student_stub = university_pb2_grpc.StudentServiceStub(channel)
    loan_stub = university_pb2_grpc.LoanServiceStub(channel)

    # --- BOOK TESTS ---
    print("\n➕ Adding a new book")
    new_book = university_pb2.Book(
        id=str(uuid.uuid4()),
        title="The Pragmatic Programmer",
        author="Andy Hunt",
        isbn="9780201616224",
        publisher="Addison-Wesley",
        pageCount=352,
        stock=4
    )
    book_stub.CreateBook(university_pb2.BookCreateRequest(book=new_book))
    print(f"✅ Book added: {new_book}")

    print("\n✏️ Updating the book")
    new_book.title = "The Pragmatic Programmer - Updated"
    book_stub.UpdateBook(university_pb2.BookUpdateRequest(book=new_book))
    print(f"✅ Book updated: {new_book}")

    # --- STUDENT TESTS ---
    print("\n➕ Adding a new student")
    new_student = university_pb2.Student(
        id=str(uuid.uuid4()),
        name="Bob Smith",
        studentNumber="20220002",
        email="bob@example.com",
        isActive=True
    )
    student_stub.CreateStudent(university_pb2.StudentCreateRequest(student=new_student))
    print(f"✅ Student added: {new_student}")

    print("\n✏️ Updating the student")
    new_student.name = "Bob Smith Jr."
    student_stub.UpdateStudent(university_pb2.StudentUpdateRequest(student=new_student))
    print(f"✅ Student updated: {new_student}")

    # --- LOAN TESTS ---
    print("\n🔁 Creating a loan")
    sample_book = book_stub.ListBooks(university_pb2.BookList()).books[0]
    sample_student = student_stub.ListStudents(university_pb2.StudentList()).students[0]
    loan = loan_stub.CreateLoan(university_pb2.LoanCreateRequest(
        studentId=sample_student.id,
        bookId=sample_book.id
    ))
    print(f"✅ Loan created: {loan.loan.id}")

    print("\n📄 Returning loan")
    returned = loan_stub.ReturnLoan(university_pb2.LoanReturnRequest(loanId=loan.loan.id))
    print(f"✅ Return date: {returned.loan.returnDate}")

    # --- DELETE TESTS ---
    print("\n❌ Deleting the student")
    student_stub.DeleteStudent(university_pb2.StudentRequest(id=new_student.id))
    print(f"✅ Student deleted: {new_student.id}")

    print("\n❌ Deleting the book")
    book_stub.DeleteBook(university_pb2.BookRequest(id=new_book.id))
    print(f"✅ Book deleted: {new_book.id}")


if __name__ == '__main__':
    run()
