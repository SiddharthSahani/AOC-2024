
from collections import deque


with open('day-15/input/part-2.txt') as f:
    grid, moves = f.read().split('\n\n')
    moves = moves.replace('\n', '')
    grid = [
        list(row.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.'))
        for row in grid.split('\n')
    ]
    NR = len(grid)
    NC = len(grid[0])

    for r in range(NR):
        for c in range(NC):
            if grid[r][c] == '@':
                grid[r][c] = '.'
                robot_r, robot_c = r, c
                break


dirs = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

for move in moves:
    dr, dc = dirs[move]
    nr, nc = robot_r + dr, robot_c + dc

    if grid[nr][nc] == '#':
        continue

    elif grid[nr][nc] == '.':
        robot_r, robot_c = nr, nc

    elif grid[nr][nc] in '[]':
        q = deque([(robot_r, robot_c)])
        seen = set()
        flag = True

        while q:
            nr, nc = q.popleft()
            if (nr, nc) in seen:
                continue

            seen.add((nr, nc))
            nnr, nnc = nr + dr, nc + dc

            if grid[nnr][nnc] == '#':
                flag = False
                break

            elif grid[nnr][nnc] == '[':
                q.append((nnr, nnc))
                q.append((nnr, nnc+1))

            elif grid[nnr][nnc] == ']':
                q.append((nnr, nnc))
                q.append((nnr, nnc-1))

        if not flag:
            continue

        while seen:
            for nr, nc in sorted(seen):
                nnr, nnc = nr + dr, nc + dc
                if (nnr, nnc) not in seen:
                    grid[nnr][nnc], grid[nr][nc] = grid[nr][nc], '.'
                    seen.remove((nr, nc))

        robot_r = robot_r + dr
        robot_c = robot_c + dc


res = sum(
    100 * r + c
    for r in range(NR)
    for c in range(NC)
    if grid[r][c] == '['
)
print(res)
