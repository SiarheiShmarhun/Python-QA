"""Removes the previous character from the string before."""


def solution(text):
    result = []

    for char in text:
        if char == "#":
            if result:
                result.pop()
        else:
            result.append(char)

    return ''.join(result)


assert solution("a#bc#d") == "bd"
assert solution("abc#d##c") == "ac"
assert solution("abc##d######") == ""
assert solution("#######") == ""
assert solution("") == ""
