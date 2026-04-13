"""Module for working with regular expressions:
   dates, passwords, and text fixing."""

import re

try:
    with open("date.txt", "r", encoding="utf-8") as file:
        content = file.read()
        text = r"(\d{2}\.\d{2}\.\d{4})"
        found_dates = re.findall(text, content)
        if found_dates:
            print("Dates found:")
            for found_date in found_dates:
                print(found_date)
        else:
            print("No dates found")

except Exception as error:   # pylint: disable=broad-exception-caught
    print(f"Error while working with file: {error}")


def check_password(password: str) -> bool:
    if (len(password) >= 8 and
            re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'\d', password)):
        return True
    return False


def fix_text(text1: str) -> str:
    new_text = r"(\b\w+\b)\s+\1"
    return re.sub(new_text, r"\1", text1, flags=re.IGNORECASE)


test_pass = "Test1234"
print(f"Password for {test_pass} correct? {check_password(test_pass)}")

sentence = "A fairly common mistake mistake is an unnecessary repetition of a word."
print(fix_text(sentence))
