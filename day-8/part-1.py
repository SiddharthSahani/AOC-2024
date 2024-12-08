
from collections import defaultdict
from itertools import combinations


with open('day-8/input/part-1.txt') as f:
    lines = f.read().splitlines()
    NR = len(lines)
    NC = len(lines[0])

    frequencies = defaultdict(list)
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char != '.':
                frequencies[char].append((r, c))


def get_antinodes(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (
        (p1[0]+dx, p1[1]+dy),
        (p2[0]-dx, p2[1]-dy),
    )


antinodes = set()

for char, positions in frequencies.items():
    for p1, p2 in combinations(positions, r=2):
        an1, an2 = get_antinodes(p1, p2)

        if an1[0] in range(NR) and an1[1] in range(NC):
            antinodes.add(an1)
        if an2[0] in range(NR) and an2[1] in range(NC):
            antinodes.add(an2)

print(len(antinodes))
