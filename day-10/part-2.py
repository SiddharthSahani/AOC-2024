
with open('day-10/input/part-2.txt') as f:
    grid = f.read().splitlines()
    NR = len(grid)
    NC = len(grid[0])

    grid = [
        [int(c) for c in line]
        for line in grid
    ]

    start_pos = []
    for i in range(NR):
        for j in range(NC):
            if grid[i][j] == 0:
                start_pos.append((i, j))


def get_score(pos, start=0):
    if start == 9:
        return 1

    score = 0

    for (di, dj) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni = pos[0] + di
        nj = pos[1] + dj
        if 0 <= ni < NR and 0 <= nj < NC and grid[ni][nj] == start+1:
            score += get_score((ni, nj), start=start+1)

    return score


score = sum(
    get_score(pos)
    for pos in start_pos
)
print(score)
