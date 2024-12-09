
from itertools import batched
from bisect import insort


with open('day-9/input/part-2.txt') as f:
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


def move_block(file_id):
    file_block = occupied[file_id]
    for free_id, free_block in enumerate(free):
        if free_block[0] > -file_block[0]:
            break
        if free_block[1] < file_block[2]:
            continue

        # print(file_block, free_block)

        if free_block[1] == file_block[2]:
            free.pop(free_id)
        else:
            free[free_id] = (free_block[0] + file_block[2], free_block[1] - file_block[2])

        occupied.pop(file_id)
        insort(occupied, (-free_block[0], file_block[1], file_block[2]))
        insort(free, (-file_block[0], file_block[2]))

        return True

    return False


while free and occupied:
    # print_line()

    for i in range(len(occupied)):
        if move_block(i):
            break
    else:
        break


# print_line()

res = 0

while occupied:
    start, bid, size = occupied.pop(0)
    res += (size * (2*-start*bid + (size-1) * bid)) // 2

print(res)
