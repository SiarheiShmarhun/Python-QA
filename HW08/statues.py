"""Counting the missing statues for the perfect collection."""
statues = [1, 3, 5, 7, 9]
minimum = min(statues)
maximum = max(statues)
needed = maximum - minimum + 1
result = needed - (len(statues))
print(result)
