"""File analysis module.
Displays information on the screen."""


import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def file(name: str) -> None:
    with open(name, 'r', encoding='utf-8') as f:
        content = f.read()
        all_lines: list[str] = content.splitlines()
    lines: int = len(all_lines)
    words: int = len(content.split())
    chars: int = len(content)
    info: str = (
        f"\nLines: {lines}\n"
        f"Words: {words}\n"
        f"Letters: {chars}\n"
    )

    logger.info("%s", info)

    with open(name, 'a', encoding='utf-8') as f:
        f.write(info)


if __name__ == "__main__":
    file("example.txt")
