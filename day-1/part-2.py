
from collections import defaultdict


with open('day-1/input/part-2.txt') as f:
    lines = f.readlines()


first_d = defaultdict(int)
second_d = defaultdict(int)

for line in lines:
    a, b = line.split()
    first_d[int(a)] += 1
    second_d[int(b)] += 1


total_dist = sum(
    num * times * second_d.get(num, 0)
    for num, times in first_d.items()
)
print(total_dist)
