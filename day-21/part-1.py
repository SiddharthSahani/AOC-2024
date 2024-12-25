
from collections import Counter


with open('day-21/input/part-1.txt') as f:
    codes = f.read().splitlines()


numeric_pad = ['789', '456', '123', ' 0A']
numeric_pad = {
    (i, j): c
    for i, line in enumerate(numeric_pad)
    for j, c in enumerate(line)
    if c != ' '
}
numeric_pad.update({
    v: k
    for k, v in numeric_pad.items()
})

directional_pad = [' ^A', '<v>']
directional_pad = {
    (i, j): c
    for i, line in enumerate(directional_pad)
    for j, c in enumerate(line)
    if c != ' '
}
directional_pad.update({
    v: k
    for k, v in directional_pad.items()
})


def step(current, target, pad):
    cp = pad[current]
    tp = pad[target]
    diff = (tp[0] - cp[0], tp[1] - cp[1])
    v_line = 'v' * diff[0] + '^' * -diff[0]
    h_line = '>' * diff[1] + '<' * -diff[1]

    if diff[1] > 0 and (tp[0], cp[1]) in pad:
        return v_line + h_line + "A"
    if (cp[0], tp[1]) in pad:
        return h_line + v_line + "A"
    if (tp[0], cp[1]) in pad:
        return v_line + h_line + "A"


def get_route(path, pad):
    c = Counter()
    start = 'A'
    for stop in path:
        c[step(start, stop, pad)] += 1
        start = stop
    return c


routes = [
    get_route(code, numeric_pad)
    for code in codes
]
for _ in range(2):
    new_rs = []
    for c in routes:
        new_r = Counter()
        for d, count in c.items():
            nc = get_route(d, directional_pad)
            for k in nc:
                nc[k] *= count
            new_r.update(nc)
        new_rs.append(new_r)
    routes = new_rs


print(sum(
    sum(
        len(k) * v
        for k, v in r.items()
    ) * int(code[:-1])
    for r, code in zip(routes, codes)
))