"""JSON module with daily log rotation."""

import json
import logging
from logging.handlers import TimedRotatingFileHandler
from os.path import exists

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        TimedRotatingFileHandler(
            "user_actions.log", when="midnight", backupCount=7, encoding="utf-8"
        )
    ]
)


def get_best_club(filename: str) -> None:
    if not exists(filename):
        logging.error("File %s not found.", filename)
        return

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            clubs = json.load(file)

        if not clubs:
            logging.warning("The list of clubs is empty.")
            return

        top_club = max(clubs, key=lambda x: x.get('wins', 0))
        logging.info("Best club: %s with %s wins",
                     top_club.get('name'), top_club.get('wins'))

    except (json.JSONDecodeError, OSError) as error:
        logging.error("Error occurred: %s", error)


if __name__ == "__main__":
    get_best_club("clubs.json")
