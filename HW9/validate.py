"""a program that accepts the recipient's number - a credit card number"""


def solution(card_number):
    card_number = str(card_number)
    if not card_number.isdigit():
        return False
    reversed_card = card_number[::-1]
    total_sum = 0
    for index, digit in enumerate(reversed_card):
        number = int(digit)
        if index % 2 != 0:
            number *= 2
            if number > 9:
                number -= 9
        total_sum += number
    return total_sum % 10 == 0


assert solution(378282246310005)
assert solution(378734493671000)
assert solution(5610591081018250)
assert not solution("456126121234546a")
assert not solution("abc")
assert not solution("")
assert not solution("4561 2612 1234 5467")
assert not solution("4561-2612-1234-5467")
assert not solution(" ")
