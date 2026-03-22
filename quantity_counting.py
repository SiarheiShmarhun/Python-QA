"""Counting the number of letters."""


def solution(text):
    if not text:
        return ''
    result = []
    counter = 1

    for index in range(len(text) - 1):
        if text[index] == text[index + 1]:
            counter += 1
        else:
            result.append(text[index])
            if counter > 1:
                result.append(str(counter))
            counter = 1
    result.append(text[-1])
    if counter > 1:
        result.append(str(counter))

    return "".join(result)


assert solution("cccbba") == "c3b2a"
assert solution("abeehhhhhccced") == "abe2h5c3ed"
assert solution("aaabbceedd") == "a3b2ce2d2"
assert solution("abcde") == "abcde"
assert solution("aaabbdefffff") == "a3b2def5"
