
with open('day-15/input/part-1.txt') as f:
    grid, instructions = f.read().split('\n\n')
    instructions = instructions.replace('\n', '')
    grid = [
        list(row)
        for row in grid.splitlines()
    ]
    NR = len(grid)
    NC = len(grid[0])


r_row = sum(i for i, row in enumerate(grid) if '@' in row)
r_col = grid[r_row].index('@')
grid[r_row][r_col] = '.'


def encounters(direction):
    offset = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0),
    }

    cr = r_row + offset[direction][0]
    cc = r_col + offset[direction][1]

    if cr in range(NR) and cc in range(NC) and grid[cr][cc] == '.':
        return (cr, cc), None

    ocr = cr
    occ = cc

    while cr in range(NR) and cc in range(NC) and grid[cr][cc] != '#':
        if grid[cr][cc] == '.':
            return (cr, cc), (ocr, occ)

        cr += offset[direction][0]
        cc += offset[direction][1]


for step in instructions:
    p = encounters(step)
    if p:
        p, op = p
        if op:
            grid[p[0]][p[1]], grid[r_row][r_col] = 'O', '.'
            r_row, r_col = op
        else:
            grid[p[0]][p[1]] = grid[r_row][r_col] = '.'
            r_row, r_col = p


res = sum(
    r*100 + c
    for r in range(NR)
    for c in range(NC)
    if grid[r][c] == 'O'
)
print(res)
