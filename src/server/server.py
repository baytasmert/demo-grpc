import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import grpc
from concurrent import futures
import uuid
from datetime import datetime
from grpc_reflection.v1alpha import reflection

import university_pb2
import university_pb2_grpc

# In-memory veri listeleri
books = []
students = []
loans = []

class BookService(university_pb2_grpc.BookServiceServicer):
    def ListBooks(self, request, context):
        return university_pb2.BooksResponse(books=books)

    def GetBook(self, request, context):
        for book in books:
            if book.id == request.id:
                return university_pb2.BookResponse(book=book)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Book not found')
        return university_pb2.BookResponse()

    def CreateBook(self, request, context):
        books.append(request.book)
        return university_pb2.BookResponse(book=request.book)

    def UpdateBook(self, request, context):
        for idx, book in enumerate(books):
            if book.id == request.book.id:
                books[idx] = request.book
                return university_pb2.BookResponse(book=request.book)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Book not found')
        return university_pb2.BookResponse()

    def DeleteBook(self, request, context):
        global books
        books = [b for b in books if b.id != request.id]
        return university_pb2.Empty()

class StudentService(university_pb2_grpc.StudentServiceServicer):
    def ListStudents(self, request, context):
        return university_pb2.StudentsResponse(students=students)

    def GetStudent(self, request, context):
        for student in students:
            if student.id == request.id:
                return university_pb2.StudentResponse(student=student)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Student not found')
        return university_pb2.StudentResponse()

    def CreateStudent(self, request, context):
        students.append(request.student)
        return university_pb2.StudentResponse(student=request.student)

    def UpdateStudent(self, request, context):
        for idx, student in enumerate(students):
            if student.id == request.student.id:
                students[idx] = request.student
                return university_pb2.StudentResponse(student=request.student)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Student not found')
        return university_pb2.StudentResponse()

    def DeleteStudent(self, request, context):
        global students
        students = [s for s in students if s.id != request.id]
        return university_pb2.Empty()

class LoanService(university_pb2_grpc.LoanServiceServicer):
    def ListLoans(self, request, context):
        return university_pb2.LoansResponse(loans=loans)

    def GetLoan(self, request, context):
        for loan in loans:
            if loan.id == request.id:
                return university_pb2.LoanResponse(loan=loan)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Loan not found')
        return university_pb2.LoanResponse()

    def CreateLoan(self, request, context):
        loan = university_pb2.Loan(
            id=str(uuid.uuid4()),
            studentId=request.studentId,
            bookId=request.bookId,
            loanDate=datetime.now().strftime("%Y-%m-%d"),
            returnDate="",
            status=university_pb2.ONGOING
        )
        loans.append(loan)
        return university_pb2.LoanResponse(loan=loan)

    def ReturnLoan(self, request, context):
        for idx, loan in enumerate(loans):
            if loan.id == request.loanId:
                updated = university_pb2.Loan(
                    id=loan.id,
                    studentId=loan.studentId,
                    bookId=loan.bookId,
                    loanDate=loan.loanDate,
                    returnDate=datetime.now().strftime("%Y-%m-%d"),
                    status=university_pb2.RETURNED
                )
                loans[idx] = updated
                return university_pb2.LoanResponse(loan=updated)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Loan not found')
        return university_pb2.LoanResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    university_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    university_pb2_grpc.add_StudentServiceServicer_to_server(StudentService(), server)
    university_pb2_grpc.add_LoanServiceServicer_to_server(LoanService(), server)

    # Reflection servisini etkinleştir
    SERVICE_NAMES = (
        university_pb2.DESCRIPTOR.services_by_name['BookService'].full_name,
        university_pb2.DESCRIPTOR.services_by_name['StudentService'].full_name,
        university_pb2.DESCRIPTOR.services_by_name['LoanService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    print("gRPC Server running at port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
