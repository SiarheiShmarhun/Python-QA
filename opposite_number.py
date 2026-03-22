"""Calculating Opposite Numbers on a Circle"""


def get_opposite_number(number: int, first_number: int):
    if number % 2 != 0:
        return None
    return (first_number + number // 2) % number


assert get_opposite_number(10, 2) == 7
assert get_opposite_number(10, 6) == 1
assert get_opposite_number(10, 4) == 9
