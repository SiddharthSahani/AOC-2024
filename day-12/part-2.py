
with open('day-12/input/part-2.txt') as f:
    grid = f.read().splitlines()
    grid = [list(line) for line in grid]
    NR = len(grid)
    NC = len(grid[0])


def get_regions():
    visited = set()

    def visit(x, y):
        c = grid[x][y]
        area = 0

        corners = {}

        stack = [(x, y)]

        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue

            area += 1
            visited.add((x, y))

            corners[(x, y)] = 0

            if x + 1 in range(NR):
                down = 0 if grid[x + 1][y] == grid[x][y] else 1
            else:
                down = 1
            if y + 1 in range(NC):
                right = 0 if grid[x][y + 1] == grid[x][y] else 1
            else:
                right = 1
            if x - 1 in range(NR):
                up = 0 if grid[x - 1][y] == grid[x][y] else 1
            else:
                up = 1
            if y - 1 in range(NC):
                left = 0 if grid[x][y - 1] == grid[x][y] else 1
            else:
                left = 1
            if x - 1 in range(NR) and y + 1 in range(NC):
                up_right = 0 if grid[x - 1][y + 1] == grid[x][y] else 1
            else:
                up_right = 1
            if x - 1 in range(NR) and y - 1 in range(NC):
                up_left = 0 if grid[x - 1][y - 1] == grid[x][y] else 1
            else:
                up_left = 1
            if x + 1 in range(NR) and y + 1 in range(NC):
                down_right = 0 if grid[x + 1][y + 1] == grid[x][y] else 1
            else:
                down_right = 1
            if x + 1 in range(NR) and y - 1 in range(NC):
                down_left = 0 if grid[x + 1][y - 1] == grid[x][y] else 1
            else:
                down_left = 1

            if left + up == 2 or (left + up == 0 and up_left):
                corners[(x, y)] += 1
            if left + down == 2 or (left + down == 0 and down_left):
                corners[(x, y)] += 1
            if right + up == 2 or (right + up == 0 and up_right):
                corners[(x, y)] += 1
            if right + down == 2 or (right + down == 0 and down_right):
                corners[(x, y)] += 1

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if x+dx in range(NR) and y+dy in range(NC) and (x+dx, y+dy) not in visited and grid[x+dx][y+dy] == c:
                    stack.append((x + dx, y + dy))

        return area, sum(corners.values())

    regions = []
    for i in range(NR):
        for j in range(NC):
            if (i, j) not in visited:
                regions.append(visit(i, j))
    return regions


cost = sum(
    area * edges
    for area, edges in get_regions()
)
print(cost)
