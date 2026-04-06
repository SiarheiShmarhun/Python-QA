"""Converts a 24-hour time string into a 12-hour format with a.m./p.m. and no leading zeros for hours."""
time_24 = "23:00"
h_str, m_str = time_24.split(":")
h = int(h_str)
hours_12 = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
new_h = hours_12[h]
periods = ["a.m.", "p.m."]
period = periods[h >= 12]
result = f"{new_h}:{m_str} {period}"
print(result)
