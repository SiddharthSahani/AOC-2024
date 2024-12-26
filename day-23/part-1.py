
from collections import defaultdict


with open('day-23/input/part-1.txt') as f:
    network = defaultdict(set)
    for line in f.read().splitlines():
        a, b = line.split('-')
        network[a].add(b)
        network[b].add(a)

all_pc = network.keys()


parties = {
    tuple(sorted((a, b, c)))
    for a in all_pc
    for b in network[a]
    for c in network[b]
    if a[0] == 't' and c in network[a]
}

print(len(parties))

