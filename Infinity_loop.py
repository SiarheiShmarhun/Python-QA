"""Checking for an infinite loop."""
a = 2
b = 6
is_infinity = False
while a != b:
    a += 1
    b -= 1
    if a > b:
        is_infinity = True
        break
print(is_infinity)
