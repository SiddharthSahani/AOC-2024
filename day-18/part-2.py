
from collections import deque
from bisect import bisect_left


with open('day-18/input/part-2.txt') as f:
    positions = [
        tuple(
            int(x)
            for x in line.split(',')
        )[::-1]
        for line in f.readlines()
    ]
    N = 70 + 1


def has_no_path(corrupted):
    visited = set()
    q = deque([((0, 0), [])])

    while q:
        pos, path = q.popleft()
        if pos in visited:
            continue

        visited.add(pos)
        path.append(pos)

        if pos == (N-1, N-1):
            break

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            r, c = pos
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in corrupted:
                q.append(((nr, nc), path[:]))

    return not q


def wrapper(position):
    index = positions.index(position)
    corrupted = set(positions[:index+1])
    return has_no_path(corrupted)


index = bisect_left(positions, True, key=lambda p: wrapper(p))
print(f"{positions[index][1]},{positions[index][0]}")
