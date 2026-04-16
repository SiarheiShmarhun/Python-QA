"""Module for checking if a number is a palindrome.
Uses logging for output as requested."""


import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def is_palindrome(integer: int) -> bool:
    string: str = str(integer)
    return string == string[::-1]


def checks() -> None:
    data: list[int] = [121, -121, 10, 0, 1001, 100]
    for number in data:
        result: bool = is_palindrome(number)
        logger.info("%s => %s", number, result)


if __name__ == "__main__":
    checks()
