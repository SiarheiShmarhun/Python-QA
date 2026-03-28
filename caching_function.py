"""Decorator that stores call results in a dictionary,
   checks whether the arguments are in the cache."""


def cache(func):
    storage = {}

    def wrapper(*args):
        if args in storage:
            return storage[args]
        result = func(*args)
        storage[args] = result
        return result
    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(5))
