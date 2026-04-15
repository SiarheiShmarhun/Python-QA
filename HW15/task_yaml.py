"""YAML module: reading and adding books to a library file."""

import logging
from os.path import exists

import yaml

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def manage_books(filename: str) -> None:
    books: list[dict] = []
    if exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                if isinstance(data, list):
                    books = data
        except (yaml.YAMLError, OSError) as err:
            logging.error("Error reading file: %s", err)
            return
    else:
        logging.info("File %s not found. A new one will be created.", filename)
    print("\n--- Adding a new book ---")
    title = input("Enter title: ")
    author = input("Enter author: ")
    try:
        year = int(input("Enter year of release: "))
    except ValueError:
        logging.error("Invalid year format. Please enter a number.")
        return
    new_book = {"title": title, "author": author, "year": year}
    books.append(new_book)
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            yaml.dump(books, file, sort_keys=False, allow_unicode=True)
        logging.info("Book '%s' successfully added to %s.", title, filename)
    except OSError as err:
        logging.error("Error saving file: %s", err)


if __name__ == "__main__":
    manage_books("books.yaml")
