# pylint: disable=import-error
"""Unit tests for the Library management system."""

import unittest

from HW12.library import Book, Reader
from logger_config import get_logger

# Используем имя логгера, как в примере преподавателя
logger = get_logger("LibraryTests")
logger.info("Library module started")


class TestLibrary(unittest.TestCase):

    def setUp(self):
        logger.info("Setting up test environment")
        self.book = Book("The Hobbit", "J.R.R. Tolkien", 400, 9780007525492)
        self.reader1 = Reader("John")
        self.reader2 = Reader("Mark")
        logger.info("Test environment set up successfully")

    def tearDown(self):
        logger.info("Tearing down test environment")
        del self.book
        del self.reader1
        del self.reader2
        logger.info("Test environment torn down successfully")

    # Positive Tests

    def test_reserve_book_success(self):
        logger.info("Testing successful book reservation")
        self.reader1.reserve_book(self.book)
        self.assertTrue(self.book.is_reserved)
        self.assertEqual(self.book.reserved_by, self.reader1)
        logger.info("Test passed successfully")

    def test_get_reserved_book_by_owner(self):
        logger.info("Testing getting book by the owner")
        self.reader1.reserve_book(self.book)
        self.reader1.get_book(self.book)
        self.assertEqual(self.book.taken_by, self.reader1)
        logger.info("Test passed successfully")

    def test_return_book_success(self):
        logger.info("Testing successful book return")
        self.reader1.get_book(self.book)
        self.reader1.return_book(self.book)
        self.assertIsNone(self.book.taken_by)
        logger.info("Test passed successfully")

    def test_cancel_reservation_success(self):
        logger.info("Testing successful reservation cancellation")
        self.reader1.reserve_book(self.book)
        self.reader1.cancel_reserve(self.book)
        self.assertFalse(self.book.is_reserved)
        logger.info("Test passed successfully")

    # Negative Tests

    def test_reserve_already_reserved_book(self):
        logger.info("Testing double reservation attempt")
        self.reader1.reserve_book(self.book)
        self.reader2.reserve_book(self.book)
        self.assertEqual(self.book.reserved_by, self.reader1)
        logger.info("Test passed successfully")

    def test_get_book_reserved_by_another(self):
        logger.info("Testing taking a book reserved by another")
        self.reader1.reserve_book(self.book)
        self.reader2.get_book(self.book)
        self.assertIsNone(self.book.taken_by)
        logger.info("Test passed successfully")

    def test_cancel_others_reservation(self):
        logger.info("Testing cancellation of someone else's reserve")
        self.reader1.reserve_book(self.book)
        self.reader2.cancel_reserve(self.book)
        self.assertTrue(self.book.is_reserved)
        logger.info("Test passed successfully")

    def test_return_others_book(self):
        logger.info("Testing return of a book taken by another")
        self.reader1.get_book(self.book)
        self.reader2.return_book(self.book)
        self.assertEqual(self.book.taken_by, self.reader1)
        logger.info("Test passed successfully")


if __name__ == '__main__':
    unittest.main()
