"""calculation of the total number of candles burned."""


def solution(candle_number, make_new):
    total_burned = candle_number
    leftovers = candle_number

    while leftovers >= make_new:
        new_made = leftovers // make_new
        remains = leftovers % make_new
        total_burned += new_made
        leftovers = new_made + remains

    return total_burned


assert solution(5, 2) == 9
assert solution(1, 2) == 1
assert solution(15, 5) == 18
assert solution(12, 2) == 23
assert solution(6, 4) == 7
assert solution(13, 5) == 16
assert solution(2, 3) == 2
