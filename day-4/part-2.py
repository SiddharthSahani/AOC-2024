
with open('day-4/input/part-2.txt') as f:
    lines = f.read().splitlines()
    NR = len(lines)
    NC = len(lines[0])


def count(r, c):
    if lines[r][c] != 'A':
        return False

    d1 = (lines[r-1][c-1] == 'M' and lines[r+1][c+1] == 'S') or (lines[r-1][c-1] == 'S' and lines[r+1][c+1] == 'M')
    d2 = (lines[r-1][c+1] == 'M' and lines[r+1][c-1] == 'S') or (lines[r-1][c+1] == 'S' and lines[r+1][c-1] == 'M')
    return d1 and d2


total = sum(
    count(r, c)
    for r in range(1, NR-1)
    for c in range(1, NC-1)
)
print(total)
