"""Module for mathematical and parity checks."""


def get_square() -> None:
    while True:
        user_input: str = input("Enter a number: ")
        try:
            number: float = float(user_input)
            print(f"Result: {number ** 2}")
            break
        except ValueError:
            print("You entered an invalid number. Try again.")


def check_even_odd() -> None:
    while True:
        user_input: str = input("Enter an integer to check for parity: ")
        try:
            number: int = int(user_input)
            if number % 2 == 0:
                print("The number is even")
            else:
                print("The number is odd")
            break
        except ValueError:
            print("You need an integer! Please enter again.")


if __name__ == "__main__":
    get_square()
    check_even_odd()
