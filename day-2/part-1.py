
from itertools import pairwise


with open('day-2/input/part-1.txt') as f:
    lines = f.readlines()


safe_count = 0

for report in lines:
    levels = list(int(elem) for elem in report.split())

    if levels[1] > levels[0]:
        is_inc = True
    else:
        is_inc = False

    is_safe = True
    for a, b in pairwise(levels):
        if is_inc:
            if b - a not in range(1, 4):
                is_safe = False
                break
        else:
            if a - b not in range(1, 4):
                is_safe = False
                break

    safe_count += is_safe

print(safe_count)
