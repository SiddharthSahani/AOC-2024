
from math import log10, ceil
from functools import cache


with open('day-11/input/part-2.txt') as f:
    stones = f.read().split()
    stones = [int(stone) for stone in stones]


@cache
def get_count(stone, iteration):
    if iteration == 0:
        return 1

    if stone == 0:
        return get_count(1, iteration-1)

    digit_count = ceil(log10(stone + 0.001))
    if digit_count % 2 == 0:
        return get_count(stone // 10**(digit_count // 2), iteration-1) + get_count(stone % 10**(digit_count // 2), iteration-1)
    else:
        return get_count(stone * 2024, iteration-1)


res = sum(
    get_count(stone, 75)
    for stone in stones
)
print(res)
