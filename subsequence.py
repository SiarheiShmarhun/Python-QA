"""Checking number sequences."""


def check_order(array: list) -> bool:
    for index in range(len(array) - 1):
        if array[index] >= array[index + 1]:
            return False
    return True


def solution(sequence: list) -> bool:
    for index in range(len(sequence) - 1):
        if sequence[index] >= sequence[index + 1]:
            option_1 = sequence[:index] + sequence[index + 1:]
            option_2 = sequence[:index+1] + sequence[index + 2:]
            return check_order(option_1) or check_order(option_2)
    return True


assert solution([1, 2, 3])
assert solution([10, 1, 2, 3])
assert solution([1, 2, 3, 0])
assert solution([-10, -5, 0])
assert not solution([1, 2, 1, 2])
assert not solution([40, 50, 60, 10, 20, 30])
assert not solution([1, 1, 1])
