
with open('day-14/input/part-1.txt') as f:
    lines = f.readlines()
    NR = 103
    NC = 101


robots = []
for line in lines:
    p, v = line.split()
    p = tuple(int(x) for x in p[2:].split(','))[::-1]
    v = tuple(int(x) for x in v[2:].split(','))[::-1]
    robots.append([p, v])


for robot in robots:
    robot[0] = (
        (robot[0][0] + robot[1][0] * 100) % NR,
        (robot[0][1] + robot[1][1] * 100) % NC,
    )


qs = [0, 0, 0, 0]
for robot in robots:
    p = robot[0]

    qs[0] += p[0] in range(NR // 2) and p[1] in range(NC // 2)
    qs[1] += p[0] in range(NR // 2) and p[1] in range(NC // 2 + 1, NC+1)
    qs[2] += p[0] in range(NR // 2 + 1, NR+1) and p[1] in range(NC // 2)
    qs[3] += p[0] in range(NR // 2 + 1, NR+1) and p[1] in range(NC // 2 + 1, NC+1)


res = qs[0] * qs[1] * qs[2] * qs[3]
print(res)
