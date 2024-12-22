
from collections import deque


with open('day-20/input/part-2.txt') as f:
    grid = [
        list(line.strip())
        for line in f.readlines()
    ]
    NR = len(grid)
    NC = len(grid[0])

    sr = sum(i for i, row in enumerate(grid) if 'S' in row)
    sc = grid[sr].index('S')
    er = sum(i for i, row in enumerate(grid) if 'E' in row)
    ec = grid[er].index('E')

    grid[sr][sc] = 0
    grid[er][ec] = '.'


q = deque([(sr, sc)])
while q:
    r, c = q.popleft()

    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr = r + dr
        nc = c + dc

        if nr in range(NR) and nc in range(NC) and grid[nr][nc] == '.':
            q.append((nr, nc))
            grid[nr][nc] = grid[r][c] + 1


count = 0

for r in range(NR):
    for c in range(NC):
        if grid[r][c] == '#':
            continue

        for nr in range(NR):
            if abs(r-nr) > 20:
                continue

            for nc in range(NC):
                if grid[nr][nc] != '#' and abs(r-nr) + abs(c-nc) <= 20 and grid[r][c] > grid[nr][nc]:
                    diff = grid[r][c] - grid[nr][nc] - (abs(r-nr) + abs(c-nc))
                    if diff >= 100:
                        count += 1

print(count)