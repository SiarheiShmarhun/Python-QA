"""Checks if the sum of current experience and reward is enough to reach or exceed the next level threshold."""
experience = 23
threshold = 27
reward = 5
lvl_up = (experience + reward) >= threshold
print(f"The next level has been reached? {lvl_up}")
