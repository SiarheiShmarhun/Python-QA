"""Module for adding one to a number
   represented as a list of digits."""


def add_one(digits: list[int]) -> list[int]:
    number: int = len(digits)
    for index in range(number - 1, - 1, - 1):
        if digits[index] < 9:
            digits[index] += 1
            return digits
        digits[index] = 0
    digits.insert(0, 1)
    return digits


print(f"[9] => {add_one([9])}")
print(f"[1, 2, 3] => {add_one([1, 2, 3])}")
print(f"[1, 1, 9] => {add_one([1, 1, 9])}")
print(f"[9, 9, 9] => {add_one([9, 9, 9])}")
