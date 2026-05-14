"""The program implements interaction between the Book and Reader objects.
   It performs the following:
   Book reservations for a specific user with double-booking protection.
   Cancellation of reservations (allowed only to the person who reserved the book).
   Book checkout with access rights and shelf availability checks.
   Returning books to the library.
   The logic is based on managing the is_reserved flag (flag) reserved_by
   and taken_by attributes."""

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


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
            logger.warning("The book %s is already reserved!", self.title)
            return
        self.is_reserved = True
        self.reserved_by = reader
        logger.info("The book %s is reserved for %s.", self.title, reader.name)

    def cancel_reserve(self, reader):
        if self.reserved_by != reader:
            logger.error("Reader %s cannot cancel someone else's reservation!", reader.name)
            return
        self.is_reserved = False
        self.reserved_by = None
        logger.info("Reservation for the book %s has been cancelled.", self.title)

    def get_book(self, reader):
        if self.is_reserved and self.reserved_by != reader:
            logger.warning("The book %s is reserved by another user!", self.title)
            return
        if self.taken_by:
            logger.warning("The book %s is already issued to another reader!", self.title)
            return
        self.taken_by = reader
        self.is_reserved = False
        self.reserved_by = None
        logger.info("The book %s is issued to %s.", self.title, reader.name)

    def return_book(self, reader):
        if self.taken_by != reader:
            logger.error("Return rejected. The book was taken by another reader!")
            return
        self.taken_by = None
        logger.info("The book %s has been returned by %s.", self.title, reader.name)


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


if __name__ == "__main__":
    book1 = Book(
        title="The Hobbit",
        author="J.R.R. Tolkien",
        pages=400,
        isbn=9780007525492
    )
    reader1 = Reader("John")
    reader2 = Reader("Mark")

    logger.info("Starting manual library tests...")
    reader1.reserve_book(book1)
    reader2.reserve_book(book1)
    reader1.cancel_reserve(book1)
    reader2.reserve_book(book1)
    reader2.get_book(book1)
    logger.info("Tests finished.")
