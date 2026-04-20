"""Task string operations."""


string = "python programming - test automation"
text_len = len(string)
print(f"String length: {text_len}")

first_char = string[0]
print(f"First character: {first_char}")

last_char = string[-1]
print(f"Last character: {last_char}")

third_from_start = string[2]
print(f"Third from start: {third_from_start}")

third_from_end = string[-3]
print(f"Third from end: {third_from_end}")

reversed_string = string[::-1]
print(f"Reversed string: {reversed_string}")

first_eight_char = string[:8]
print(f"First eight character: {first_eight_char}")
