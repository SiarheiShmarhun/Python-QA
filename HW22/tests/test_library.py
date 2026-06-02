"""Unit tests for the Library management system using Stubs, Fakes, Mocks, and Flaky markers."""

import pytest
from logger_config import get_logger

logger = get_logger(__name__)


class BookStub:

    def __init__(self, title, author=None, pages=None, isbn=None):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = False
        self.reserved_by = None
        self.taken_by = None


class FakeReader:

    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        if not book.is_reserved:
            book.is_reserved = True
            book.reserved_by = self

    def cancel_reserve(self, book):
        if book.is_reserved and book.reserved_by == self:
            book.is_reserved = False
            book.reserved_by = None

    def get_book(self, book):
        if not book.is_reserved or book.reserved_by == self:
            book.taken_by = self

    def return_book(self, book):
        if book.taken_by == self:
            book.taken_by = None


@pytest.fixture(name="book")
def fixture_book():
    return BookStub("The Hobbit", "J.R.R. Tolkien", 400, 9780007525492)


@pytest.fixture(name="reader1")
def fixture_reader1():
    return FakeReader("John")


@pytest.fixture(name="reader2")
def fixture_reader2():
    return FakeReader("Mark")


# Positive Tests


def test_reserve_book_success(book, reader1):
    logger.info("Testing successful book reservation using Fake Reader")
    reader1.reserve_book(book)
    assert book.is_reserved is True
    assert book.reserved_by == reader1
    logger.info("Test passed successfully")


def test_get_reserved_book_by_owner(book, reader1):
    logger.info("Testing getting book by the owner using Fake Reader")
    reader1.reserve_book(book)
    reader1.get_book(book)
    assert book.taken_by == reader1
    logger.info("Test passed successfully")


@pytest.mark.flaky(reruns=3, reruns_delay=1)
def test_return_book_success(book, reader1):
    logger.info("Testing successful book return (Flaky test)")

    if not hasattr(test_return_book_success, "attempts"):
        test_return_book_success.attempts = 0

    test_return_book_success.attempts += 1

    if test_return_book_success.attempts == 1:
        logger.warning("Flaky test simulated failure on the first attempt!")
        raise RuntimeError("Library database timeout")
    reader1.get_book(book)
    reader1.return_book(book)
    assert book.taken_by is None
    logger.info("Test passed successfully")


def test_cancel_reservation_success(mocker, book):
    logger.info("Testing successful reservation cancellation using Mock")
    mock_reader = mocker.Mock()
    mock_reader.cancel_reserve(book)
    mock_reader.cancel_reserve.assert_called_once_with(book)
    logger.info("Test passed successfully")


# Negative Tests


def test_reserve_already_reserved_book(book, reader1, reader2):
    logger.info("Testing double reservation attempt on Fake Reader")
    reader1.reserve_book(book)
    reader2.reserve_book(book)
    assert book.reserved_by == reader1
    logger.info("Test passed successfully")


def test_get_book_reserved_by_another(book, reader1, reader2):
    logger.info("Testing taking a book reserved by another on Fake Reader")
    reader1.reserve_book(book)
    reader2.get_book(book)
    assert book.taken_by is None
    logger.info("Test passed successfully")


def test_cancel_others_reservation(book, reader1, reader2):
    logger.info("Testing cancellation of someone else's reserve on Fake Reader")
    reader1.reserve_book(book)
    reader2.cancel_reserve(book)
    assert book.is_reserved is True
    logger.info("Test passed successfully")


def test_return_others_book(book, reader1, reader2):
    logger.info("Testing return of a book taken by another on Fake Reader")
    reader1.get_book(book)
    reader2.return_book(book)
    assert book.taken_by == reader1
    logger.info("Test passed successfully")
