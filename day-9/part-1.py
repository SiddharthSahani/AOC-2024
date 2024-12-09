
from itertools import batched
from bisect import insort


with open('day-9/input/part-1.txt') as f:
    line = f.read()
    if len(line) % 2 == 1:
        line += '0'


occupied = []
free = []

s = 0
for i, (a, b) in enumerate(batched(line, n=2)):
    insort(occupied, (-s, i, int(a)))
    s += int(a)
    if b != '0':
        insort(free, (s, int(b)))
        s += int(b)


def print_line():
    for block in sorted(occupied + free, key=lambda item: abs(item[0])):
        if len(block) == 3:
            print(f"{block[1]}"*block[2], end='')
        else:
            print("."*block[1], end='')
    print()


while free and occupied:
    # print_line()

    start, size = free[0]
    if start > -occupied[0][0]:
        break

    if size <= occupied[0][2]:
        free.pop(0)
        insort(occupied, (-start, occupied[0][1], size))
        if size == occupied[0][2]:
            occupied.pop(0)
        else:
            occupied[0] = (occupied[0][0], occupied[0][1], occupied[0][2] - size)
    else:
        block = occupied.pop(0)
        free[0] = (start + block[2], size - block[2])
        insort(occupied, (-start, block[1], block[2]))


# print_line()

res = 0

while occupied:
    start, bid, size = occupied.pop(0)
    res += (size * (2*-start*bid + (size-1) * bid)) // 2

print(res)
