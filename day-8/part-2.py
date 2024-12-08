
from collections import defaultdict
from itertools import combinations


with open('day-8/input/part-2.txt') as f:
    lines = f.read().splitlines()
    NR = len(lines)
    NC = len(lines[0])

    frequencies = defaultdict(list)
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char not in '.#':
                frequencies[char].append((r, c))


def get_antinodes(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]

    res = []

    i = 0
    while p1[0] + i*dx in range(NR) and p1[1] + i*dy in range(NC):
        res.append((p1[0]+i*dx, p1[1]+i*dy))
        i += 1

    i = 0
    while p2[0] - i*dx in range(NR) and p2[1] - i*dy in range(NC):
        res.append((p2[0]-i*dx, p2[1]-i*dy))
        i += 1

    return res


antinodes = set()

for char, positions in frequencies.items():
    for p1, p2 in combinations(positions, r=2):
        res = get_antinodes(p1, p2)
        antinodes.update(res)

print(len(antinodes))
