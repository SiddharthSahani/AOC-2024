
with open('day-1/input/part-1.txt') as f:
    lines = f.readlines()

first_l = []
second_l = []

for line in lines:
    a, b = line.split()
    first_l.append(int(a))
    second_l.append(int(b))

first_l.sort()
second_l.sort()


total_dist = sum(
    abs(a - b)
    for a, b in zip(first_l, second_l)
)
print(total_dist)
