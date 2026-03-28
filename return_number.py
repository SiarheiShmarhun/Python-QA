"""Decorator calls a function and checks
   whether the result is a number
   (int or float). If the result is of another type,
   an error message is displayed,
   but program execution continues."""


def check_result_type(func):
    def wrapper(*args):
        result = func(*args)
        if not isinstance(result, (int, float)):
            print("Error: result is not a number")
        return result
    return wrapper


@check_result_type
def get_result(data):
    return data


print(get_result(150))
print(get_result(34.3))
print(get_result("text"))
