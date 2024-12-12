
with open('day-12/input/part-1.txt') as f:
    grid = f.read().splitlines()
    grid = [list(line) for line in grid]
    NR = len(grid)
    NC = len(grid[0])


def get_regions():
    visited = set()

    def visit(x, y):
        c = grid[x][y]
        area = 0
        perimeter = 0

        stack = [(x, y)]

        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue

            area += 1
            perimeter += 4
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (x+dx, y+dy) in visited and grid[x+dx][y+dy] == c:
                    perimeter -= 2

            visited.add((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if x+dx in range(NR) and y+dy in range(NC) and (x+dx, y+dy) not in visited and grid[x+dx][y+dy] == c:
                    stack.append((x + dx, y + dy))

        return area, perimeter

    regions = []
    for i in range(NR):
        for j in range(NC):
            if (i, j) not in visited:
                regions.append(visit(i, j))
    return regions


cost = sum(
    area * perimeter
    for area, perimeter in get_regions()
)
print(cost)
