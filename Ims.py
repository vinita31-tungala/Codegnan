class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Year: {self.year}")


class PrintedBook(Book):
    def __init__(self, book_id, title, author, pages):
        super().__init__(book_id, title, author, None)
        self.pages = pages

    def display(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


class EBook(Book):
    def __init__(self, book_id, title, author, file_size):
        super().__init__(book_id, title, author, None)
        self.file_size = file_size

    def display(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, File Size: {self.file_size}")

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book in self.borrowed_books:
            print(f"'{book.title}' is already borrowed.")
        else:
            self.borrowed_books.append(book)
            print(f"'{self.name}' borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"'{self.name}' returned '{book.title}'.")
        else:
            print(f"'{self.name}' has not borrowed '{book.title}'.")

    def display_member(self):
        print(f"ID: {self.member_id}, Name: {self.name}")

class StudentMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)

    def display_member(self):
        print(f"Student ID: {self.member_id}, Name: {self.name}")

class FacultyMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)

    def display_member(self):
        print(f"Faculty ID: {self.member_id}, Name: {self.name}")

class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
        self.members=[]
    #Add book
    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")
    #remove book
    def remove_book(self,book_id):
        for book in self.books:
            if book.book_id==book_id:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"Book with ID '{book_id}' not found in the library.")
    #register member
    def register_member(self,member):
        self.members.append(member)
        print(f"Member '{member.name}' registered in the library.")
    #search book
    def search_book(self,title=None,author=None):
        found=False
        for book in self.books:
            if(title and title.lower() in book.title.lower()):
                book.display()
                found=True
            elif(author and author.lower() in book.author.lower()):
                book.display()
                found=True
        if not found:
            print("No books found matching the search criteria.")
    #display books
    def display_books(self):
        print("\n Library books:")
        if not self.books:
            print("No books available")
            return
        for book in self.books:
            book.display()
    #display members
    def display_members(self):
        print("\n Library members:")
        for member in self.members:
            member.display_member()
    #find member
    def find_member(self,member_id):
        for member in self.members:
            if member.member_id==member_id:
                return member
        return None
    #find book
    def find_book(self,book_id):
        for book in self.books:
            if book.book_id==book_id:
                return book
        return None
library=Library("XYZ Central Library")
book1=Book(1,"The Great Gatsby","F. Scott Fitzgerald",1925)
book2=PrintedBook(2,"To Kill a Mockingbird","Harper Lee",200)
book3=EBook(3,"1984","George Orwell","10MB")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
student=StudentMember(1,"John Doe")
faculty=FacultyMember(2,"Dr. Smith")
library.register_member(student)
library.register_member(faculty)
library.display_books()
student.borrow_book(book1)
student.display_member()
student.return_book(book1)
library.search_book(title="1984")
library.search_book(author="Harper Lee")




