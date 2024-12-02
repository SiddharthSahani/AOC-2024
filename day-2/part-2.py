
from itertools import pairwise


with open('day-2/input/part-2.txt') as f:
    lines = f.readlines()


def is_safe(levels):
    if levels[1] > levels[0]:
        is_inc = True
    else:
        is_inc = False

    for a, b in pairwise(levels):
        if is_inc:
            if b - a not in range(1, 4):
                return False
        else:
            if a - b not in range(1, 4):
                return False

    return True


safe_count = 0

for report in lines:
    levels = list(int(elem) for elem in report.split())

    if is_safe(levels):
        safe_count += 1
    else:
        for i in range(len(levels)):
            levels_c = levels[:]
            levels_c.pop(i)
            if is_safe(levels_c):
                safe_count += 1
                break

print(safe_count)
