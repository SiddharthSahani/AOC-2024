
from collections import defaultdict
from functools import reduce


with open('day-23/input/part-2.txt') as f:
    network = defaultdict(set)
    for line in f.read().splitlines():
        a, b = line.split('-')
        network[a].add(b)
        network[b].add(a)

all_pc = network.keys()


cache = {}
def get_max(mems):
    fr_mems = frozenset(mems)
    if fr_mems in cache:
        cache[fr_mems][1] += 1
        return cache[fr_mems][0]

    others = reduce(
        lambda a, b: a & network[b],
        mems,
        all_pc
    )
    max_mems = mems
    for o in others:
        o_mems = get_max(mems | {o})
        if len(o_mems) > len(max_mems):
            max_mems = o_mems
        
    cache[fr_mems] = [max_mems, 0]
    return max_mems


res = set()
for pc in all_pc:
    mems = get_max({pc})
    if len(mems) > len(res):
        res = mems

print(','.join(sorted(res)))
