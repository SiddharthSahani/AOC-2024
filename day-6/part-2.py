
with open('day-6/input/part-2.txt') as f:
    f_content = f.read()
    grid = f_content.split('\n')

    NR = len(grid)
    NC = len(grid[0])

    start_row = sum(
        i
        for i, row in enumerate(grid)
        if '^' in row
    )
    start_col = grid[start_row].index('^')


dirs = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}


def get_path():
    path = set()
    cur_dir = (-1, 0)
    cur_row, cur_col = start_row, start_col
    visited = set([(cur_row, cur_col)])

    while cur_row in range(NR) and cur_col in range(NC):
        next_row, next_col = cur_row + cur_dir[0], cur_col + cur_dir[1]
        path.add((cur_row, cur_col))
        if next_row in range(NR) and next_col in range(NC):
            if grid[next_row][next_col] == '#':
                cur_dir = dirs[cur_dir]
            else:
                cur_row, cur_col = next_row, next_col
                visited.add((cur_row, cur_col))
        else:
            break

    return path


path = get_path()
count = 0

for i, j in path:
    cur_row, cur_col = start_row, start_col
    cur_dir = (-1, 0)
    visited = set()

    while cur_row in range(NR) and cur_col in range(NC):
        if (cur_row, cur_col, cur_dir) in visited:
            count += 1
            break

        visited.add((cur_row, cur_col, cur_dir))
        next_row, next_col = cur_row + cur_dir[0], cur_col + cur_dir[1]
        if next_row in range(NR) and next_col in range(NC):
            if grid[next_row][next_col] == '#':
                cur_dir = dirs[cur_dir]
            elif next_row == i and next_col == j:
                cur_dir = dirs[cur_dir]
            else:
                cur_row, cur_col = next_row, next_col
        else:
            break

print(count)
