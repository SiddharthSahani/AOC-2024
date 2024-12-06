
with open('day-6/input/part-1.txt') as f:
    f_content = f.read()
    grid = f_content.split('\n')

    NR = len(grid)
    NC = len(grid[0])

    cur_row = sum(
        i
        for i, row in enumerate(grid)
        if '^' in row
    )
    cur_col = grid[cur_row].index('^')


dirs = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}

cur_dir = (-1, 0)
visited = set([(cur_row, cur_col)])


while cur_row in range(NR) and cur_col in range(NC):
    next_row, next_col = cur_row + cur_dir[0], cur_col + cur_dir[1]
    if next_row in range(NR) and next_col in range(NC):
        if grid[next_row][next_col] == '#':
            cur_dir = dirs[cur_dir]
        else:
            cur_row, cur_col = next_row, next_col
            visited.add((cur_row, cur_col))
    else:
        break

print(len(visited))
