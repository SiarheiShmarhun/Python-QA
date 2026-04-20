"""Module for checking if a number is a palindrome.
Uses logging for output as requested."""


import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def is_palindrome(integer: int) -> bool:
    string: str = str(integer)
    return string == string[::-1]


assert is_palindrome(121)
assert not is_palindrome(-121)
assert not is_palindrome(10)
assert is_palindrome(0)
assert is_palindrome(1001)
assert not is_palindrome(100)
