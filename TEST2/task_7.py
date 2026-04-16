"""Module for string pattern transformation."""


import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def transform_string(source: str, limit: int) -> str:
    prefix: str = source[:limit]
    suffix: str = prefix[:-1][::-1]
    return prefix + suffix


if __name__ == "__main__":
    text: str = "Module for string pattern transformation"
    for index in range(1, 5):
        result = transform_string(text, index)
        logger.info("Result for %s: %s", index, result)
