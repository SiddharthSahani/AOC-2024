
with open('day-4/input/part-1.txt') as f:
    lines = f.read().splitlines()
    NR = len(lines)
    NC = len(lines[0])


def count(r, c):
    def search_direction(dr, dc):
        for i, char in enumerate('MAS', start=1):
            nr = r + dr * i
            nc = c + dc * i
            if 0 <= nr < NR and 0 <= nc < NC:
                if lines[nr][nc] != char:
                    break
                elif i == 3:
                    return True
            else:
                break
        return False

    if lines[r][c] != 'X':
        return 0

    return (
        search_direction(-1, -1) + search_direction(+0, -1) + search_direction(+1, -1) +
        search_direction(-1, +0) +                          + search_direction(+1, +0) +
        search_direction(-1, +1) + search_direction(+0, +1) + search_direction(+1, +1)
    )


total = sum(
    count(r, c)
    for r in range(NR)
    for c in range(NC)
)
print(total)
