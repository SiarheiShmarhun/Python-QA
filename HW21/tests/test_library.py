"""Unit tests for the Library management system using PyTest."""

import pytest
from HW12.library import Book, Reader
from logger_config import get_logger

logger = get_logger(__name__)


@pytest.fixture
def book():
    return Book("The Hobbit", "J.R.R. Tolkien", 400, 9780007525492)


@pytest.fixture
def reader1():
    return Reader("John")


@pytest.fixture
def reader2():
    return Reader("Mark")


# Positive Tests


def test_reserve_book_success(book, reader1):
    logger.info("Testing successful book reservation")
    reader1.reserve_book(book)
    assert book.is_reserved is True
    assert book.reserved_by == reader1
    logger.info("Test passed successfully")


def test_get_reserved_book_by_owner(book, reader1):
    logger.info("Testing getting book by the owner")
    reader1.reserve_book(book)
    reader1.get_book(book)
    assert book.taken_by == reader1
    logger.info("Test passed successfully")


def test_return_book_success(book, reader1):
    logger.info("Testing successful book return")
    reader1.get_book(book)
    reader1.return_book(book)
    assert book.taken_by is None
    logger.info("Test passed successfully")


def test_cancel_reservation_success(book, reader1):
    logger.info("Testing successful reservation cancellation")
    reader1.reserve_book(book)
    reader1.cancel_reserve(book)
    assert book.is_reserved is False
    logger.info("Test passed successfully")


# Negative Tests


def test_reserve_already_reserved_book(book, reader1, reader2):
    logger.info("Testing double reservation attempt")
    reader1.reserve_book(book)
    reader2.reserve_book(book)
    assert book.reserved_by == reader1
    logger.info("Test passed successfully")


def test_get_book_reserved_by_another(book, reader1, reader2):
    logger.info("Testing taking a book reserved by another")
    reader1.reserve_book(book)
    reader2.get_book(book)
    assert book.taken_by is None
    logger.info("Test passed successfully")


def test_cancel_others_reservation(book, reader1, reader2):
    logger.info("Testing cancellation of someone else's reserve")
    reader1.reserve_book(book)
    reader2.cancel_reserve(book)
    assert book.is_reserved is True
    logger.info("Test passed successfully")


def test_return_others_book(book, reader1, reader2):
    logger.info("Testing return of a book taken by another")
    reader1.get_book(book)
    reader2.return_book(book)
    assert book.taken_by == reader1
    logger.info("Test passed successfully")
