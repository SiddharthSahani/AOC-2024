
import heapq


with open('day-16/input/part-2.txt') as f:
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


def func(q, backward):
    visited = set()
    dist = {}

    while q:
        cost, cur_pos, cur_dir = heapq.heappop(q)
        if (cur_pos, cur_dir) in visited:
            continue

        dist[(cur_pos, cur_dir)] = cost
        visited.add((cur_pos, cur_dir))

        if not backward and cur_pos == end_pos:
            return dist, cost

        if backward:
            dr, dc = dirs[(cur_dir + 2) % 4]
        else:
            dr, dc = dirs[cur_dir]
        next_pos = (cur_pos[0] + dr, cur_pos[1] + dc)

        if next_pos[0] in range(NR) and next_pos[1] in range(NC) and grid[next_pos[0]][next_pos[1]] != '#':
            heapq.heappush(q, (cost + 1, next_pos, cur_dir))

        # clockwise
        heapq.heappush(q, (cost + 1000, cur_pos, (cur_dir + 1) % 4))
        # counter-clockwise
        heapq.heappush(q, (cost + 1000, cur_pos, (cur_dir + 3) % 4))

    return dist


d1, best = func([(0, start_pos, 1)], backward=False)
d2 = func(
    [(0, end_pos, i) for i in range(4)],
    backward=True
)

seats = set()

for i in range(NR):
    for j in range(NC):
        for d in range(4):
            c1 = d1.get(((i, j), d), 0)
            c2 = d2.get(((i, j), d), 0)
            if c1 + c2 == best:
                seats.add((i, j))

print(len(seats))
