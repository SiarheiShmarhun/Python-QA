"""A program for working with dates:
   calculating the difference and comparing it with the current date."""
from datetime import datetime


def get_valid_date(date_str: str) -> str:
    while True:
        user_input = input(date_str)
        try:
            datetime.strptime(user_input, "%Y-%m-%d")
            return user_input
        except ValueError:
            print("Error: Invalid date format! Use YYYY-MM-DD")


def get_days_between(date1: str, date2: str) -> int:
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def check_date(date_str: str) -> str:
    input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    today = datetime.now().date()
    if input_date > today:
        return "The date is in the future."
    if input_date < today:
        return "The date is in the past."
    return "The date is today"


try:
    print("--- Difference between dates ---")
    date_user1 = get_valid_date("Please enter the first date (YYYY-MM-DD): ")
    date_user2 = get_valid_date("Please enter the second date (YYYY-MM-DD): ")
    result = get_days_between(date_user1, date_user2)
    print(f"Number of days between dates: {result}")
    print("\n--- Past or Future check ---")
    date_check = get_valid_date("Enter a date to check (YYYY-MM-DD): ")
    print(check_date(date_check))

except Exception as error:     # pylint: disable=broad-exception-caught
    print(f"An unexpected error occurred: {error}")
