
from collections import defaultdict


with open('day-5/input/part-1.txt') as f:
    f_content = f.read()
    section_1, section_2 = f_content.split('\n\n')
    section_1 = section_1.splitlines()
    section_2 = section_2.splitlines()


dependencies = defaultdict(set)

for line in section_1:
    a, b = line.split('|')
    dependencies[b].add(a)


def is_valid(nums):
    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums[i+1:], start=i+1):
            if n2 in dependencies[n1]:
                return False

    return True


total = 0

for line in section_2:
    nums = line.split(',')
    if is_valid(nums):
        total += int(nums[len(nums)//2])

print(total)