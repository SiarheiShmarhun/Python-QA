"""Converts a string containing a molecular formula into
   a dictionary containing the counted number of atoms."""


def parse_molecule(formula: str) -> dict:
    stack: list[dict] = [{}]
    i = 0
    while i < len(formula):
        char = formula[i]
        if char in "([{":
            stack.append({})
            i += 1
        elif char in ")]}":
            i += 1
            num = ""
            while i < len(formula) and formula[i].isdigit():
                num += formula[i]
                i += 1
            multiplier = int(num) if num else 1
            inner: dict = stack.pop()
            for atom, count in inner.items():
                stack[-1][atom] = stack[-1].get(atom, 0) + count * multiplier
        elif char.isupper():
            atom = char
            i += 1
            while i < len(formula) and formula[i].islower():
                atom += formula[i]
                i += 1
            num = ""
            while i < len(formula) and formula[i].isdigit():
                num += formula[i]
                i += 1
            count = int(num) if num else 1
            stack[-1][atom] = stack[-1].get(atom, 0) + count
        else:
            i += 1
    return stack[0]


print(parse_molecule("H2O"))
print(parse_molecule("Mg(OH)2"))
print(parse_molecule("K4[ON(SO3)2]2"))
