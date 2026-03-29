"""The program implements interaction between the Book and Reader objects.
   It performs the following:
   Book reservations for a specific user with double-booking protection.
   Cancellation of reservations (allowed only to the person who reserved the book).
   Book checkout with access rights and shelf availability checks.
   Returning books to the library.
   The logic is based on managing the is_reserved flag (flag) reserved_by
   and taken_by attributes."""


class Book:

    def __init__(self, title, author, pages, isbn):
        self.is_reserved = False
        self.reserved_by = None
        self.taken_by = None
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn

    def reserve(self, reader):
        if self.is_reserved:
            print(f"The book {self.title} already reserved!")
            return
        self.is_reserved = True
        self.reserved_by = reader
        print(f"The book {self.title} is reserved for {self.reserved_by.name}.")

    def cancel_reserve(self, reader):
        if self.reserved_by != reader:
            print("You can't cancel someone else's reservation!")
            return
        self.is_reserved = False
        self.reserved_by = None
        print(f"The reservation for the book {self.title} has been cancelled.")

    def get_book(self, reader):
        if self.is_reserved and self.reserved_by != reader:
            print("The book has been reserved by another user!")
            return
        if self.taken_by:
            print("The book has already been issued to another reader!")
            return
        self.taken_by = reader
        self.is_reserved = False
        self.reserved_by = None
        print(f"The Book {self.title} is issued to {reader.name}.")

    def return_book(self, reader):
        if self.taken_by != reader:
            print(f"Return rejected. The Book {reader.name}, was taken by another reader!")
            return
        self.taken_by = None
        print(f"The Book {self.title} has been successfully returned by {reader.name}.")


class Reader:

    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        book.reserve(self)

    def cancel_reserve(self, book):
        book.cancel_reserve(self)

    def get_book(self, book):
        book.get_book(self)

    def return_book(self, book):
        book.return_book(self)


book1 = Book(
    title="The Hobbit",
    author="Books by J.R.R. Tolkien",
    pages=400,
    isbn=9780007525492
)

reader1 = Reader("John")
reader2 = Reader("Mark")


print(book1.title)
reader1.reserve_book(book1)
reader2.reserve_book(book1)
reader1.cancel_reserve(book1)
reader2.reserve_book(book1)
reader1.get_book(book1)
reader2.get_book(book1)
reader1.return_book(book1)
reader2.return_book(book1)
reader1.get_book(book1)
