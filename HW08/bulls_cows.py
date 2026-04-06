"""Bulls and Cows: 4-digit number guessing game."""
import random

digits = random.sample("0123456789", 4)
secret_number = "".join(digits)
cow_forms = ['коров', 'корова', 'коровы', 'коровы', 'коровы']
bull_forms = ['быков', 'бык', 'быка', 'быка', 'быка']
bull_numbers = ['ноль', 'один', 'два', 'три', 'четыре']
cow_numbers = ['ноль', 'одна', 'две', 'три', 'четыре']


def get_number(number, secret):
    b_count = 0
    c_count = 0
    for index, digit in enumerate(number):
        if digit == secret[index]:
            b_count += 1
        elif digit in secret:
            c_count += 1
    return b_count, c_count


def validate_input(number):
    return len(number) == 4 and number.isdigit() and len(set(number)) == 4


while True:
    player_number = input('Введите 4-значное число с неповторяющимися цифрами: ')
    if not validate_input(player_number):
        print("Ошибка! Введите 4 разные цифры. ")
        continue
    bulls, cows = get_number(player_number, secret_number)
    if bulls == 4:
        print('Вы выиграли')
        break
    result = f"{cow_numbers[cows]} {cow_forms[cows]}, {bull_numbers[bulls]} {bull_forms[bulls]}"
    print(result.capitalize())
