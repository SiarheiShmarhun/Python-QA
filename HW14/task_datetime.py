"""A program for working with dates:
   calculating the difference and comparing it with the current date."""
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO,format='%(message)s')

def get_valid_date(date_str: str) -> datetime:
    while True:
        user_input = input(date_str)
        try:
            return datetime.strptime(user_input, "%Y-%m-%d")
        except ValueError:
            logging.error("Error: Invalid date format! Use YYYY-MM-DD")


def get_days_between(date1: datetime, date2: datetime) -> int:
    return abs((date2 - date1).days)


def check_date(input_date: datetime) -> str:
    today = datetime.now().date()
    if input_date.date() > today:
        return "The date is in the future."
    if input_date.date() < today:
        return "The date is in the past."
    return "The date is today"


try:
    logging.info("--- Difference between dates ---")
    date_user1 = get_valid_date("Please enter the first date (YYYY-MM-DD): ")
    date_user2 = get_valid_date("Please enter the second date (YYYY-MM-DD): ")
    result = get_days_between(date_user1, date_user2)
    logging.info(f"Number of days between dates: {result}")
    logging.info("\n--- Past or Future check ---")
    date_check = get_valid_date("Enter a date to check (YYYY-MM-DD): ")
    logging.info(check_date(date_check))

except Exception as error:     # pylint: disable=broad-exception-caught
    logging.error(f"An unexpected error occurred: {error}")
