
import heapq


with open('day-16/input/part-1.txt') as f:
    grid = f.read().splitlines()
    NR = len(grid)
    NC = len(grid[0])


for i in range(NR):
    for j in range(NC):
        if grid[i][j] == 'S':
            start_pos = (i, j)
        if grid[i][j] == 'E':
            end_pos = (i, j)


dirs = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


visited = set()
q = [(0, start_pos, 1)]
dist = {}

while q:
    cost, cur_pos, cur_dir = heapq.heappop(q)
    if (cur_pos, cur_dir) in visited:
        continue

    dist[(cur_pos, cur_dir)] = cost
    visited.add((cur_pos, cur_dir))

    if cur_pos == end_pos:
        print(cost)
        break

    dr, dc = dirs[cur_dir]
    next_pos = (cur_pos[0] + dr, cur_pos[1] + dc)

    if next_pos[0] in range(NR) and next_pos[1] in range(NC) and grid[next_pos[0]][next_pos[1]] != '#':
        heapq.heappush(q, (cost + 1, next_pos, cur_dir))

    # clockwise
    heapq.heappush(q, (cost + 1000, cur_pos, (cur_dir + 1) % 4))
    # counter-clockwise
    heapq.heappush(q, (cost + 1000, cur_pos, (cur_dir + 3) % 4))
