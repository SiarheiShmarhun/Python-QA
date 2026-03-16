"""Returns the sum of the digits of the current time (HH:MM) after n minutes have passed since midnight."""
n = 270
hours = n // 60
minutes = n % 60
time_str = f"{hours:02d}{minutes:02d}"
result = int(time_str[0]) + int(time_str[1]) + int(time_str[2]) + int(time_str[3])
print(result)
