"""Module for calculating the sum of
   all numbers up to a given limit."""


def calculate_sum() -> None:
    while True:
        user_input: str = input("Enter a positive integer: ")
        try:
            limit = int(user_input)
            if limit < 1:
                print("Enter a number greater than 0.")
                continue
            total: int = 0
            for i in range(1, limit + 1):
                total += i
            print(f"The sum of numbers up to {limit} is: {total}")
            break
        except ValueError:
            print("Invalid input. Enter an integer.")


if __name__ == "__main__":
    calculate_sum()
