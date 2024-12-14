
with open('day-14/input/part-2.txt') as f:
    lines = f.readlines()
    NR = 103
    NC = 101


grid = [[0] * NC for _ in range(NR)]

robots = []
for line in lines:
    p, v = line.split()
    p = tuple(int(x) for x in p[2:].split(','))[::-1]
    v = tuple(int(x) for x in v[2:].split(','))[::-1]
    robots.append([p, v])
    grid[p[0]][p[1]] += 1


def func():
    def dfs(robot_idx):
        count = 0
        stack = [robots[robot_idx][0]]

        while stack:
            p = stack.pop()
            if p in visited:
                continue

            visited.add(p)
            count += 1

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                p2 = p[0] + dx, p[1] + dy
                if p2[0] in range(NR) and p2[1] in range(NC) and p2 not in visited and grid[p2[0]][p2[1]]:
                    stack.append(p2)

        return count

    visited = set()
    return max(dfs(i) for i in range(len(robots)))


max_i = 0
max_count = 0
MAX_ITER = 10_000

for i in range(MAX_ITER):
    if i % 1000 == 0:
        print(f'{i / MAX_ITER * 100:.2f}% done')

    for robot in robots:
        grid[robot[0][0]][robot[0][1]] -= 1
        robot[0] = (
            (robot[0][0] + robot[1][0]) % NR,
            (robot[0][1] + robot[1][1]) % NC,
        )
        grid[robot[0][0]][robot[0][1]] += 1

    count = func()
    if count > max_count:
        max_count = count
        max_i = i + 1


for robot in robots:
    robot[0] = (
        (robot[0][0] + robot[1][0] * (max_i - i - 1)) % NR,
        (robot[0][1] + robot[1][1] * (max_i - i - 1)) % NC,
    )


for i in range(NR):
    for j in range(NC):
        if any(robot[0] == (i, j) for robot in robots):
            print('#', end='')
        else:
            print('.', end='')
    print()

print(max_i)
