"""Decorator takes a data type,
   loops through all the incoming function arguments,
   converts them to that type, and passes the updated
   data back to the original function."""


def typed(type_):
    def decorator(func):
        def wrapper(*args):
            new_args = []
            for arg in args:
                new_args.append(type_(arg))
            return func(*new_args)
        return wrapper
    return decorator


@typed(type_=str)
def add_string(a, b):
    return a + b


@typed(type_=int)
def add_ints(a, b, c):
    return a + b + c


@typed(type_=float)
def add_floats(a, b, c):
    return a + b + c


print(add_string("3", 5))
print(add_string('a', 'b'))
print(add_ints(5, 6, 7))
print(add_floats(0.1, 0.2, 0.4))
