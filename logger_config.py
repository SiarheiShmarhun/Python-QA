"""Module for centralized logging configuration."""

import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        logger.addHandler(console_handler)

    return logger
