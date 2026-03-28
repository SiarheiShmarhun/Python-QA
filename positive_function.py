"""The decorator iterates through all incoming arguments,
   and checks whether they are positive numbers.
   If it encounters a number less than or equal to zero,
   a ValueError is thrown."""


def validate_arguments(func):
    def wrapper(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError("Number must be greater than 0")
        return func(*args)
    return wrapper


@validate_arguments
def get_result(data):
    return data


print(get_result(3))
print(get_result(5.5))
print(get_result(-7))
print(get_result(24))
