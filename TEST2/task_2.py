"""Module for mathematical and parity checks."""


def get_square(number: int) -> int:
    return number ** 2


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False


while True:
    try:
        user_input: int = int(input("Enter a number: "))
        break
    except ValueError:
        print("You entered an invalid number. Try again.")
print(f"Square of the number: {get_square(user_input)}")
if is_even(user_input):
    print("Number is even.")
else:
    print("Number is odd.")
