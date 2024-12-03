
import re


with open('day-3/input/part-2.txt') as f:
    file_content = f.read()


pattern = re.compile(r"mul\(-*\d+,-*\d+\)|don't\(\)|do\(\)")

s = 0
enabled = True
for match in re.finditer(pattern, file_content):
    if match.group() == 'do()':
        enabled = True
    elif match.group() == "don't()":
        enabled = False
    elif enabled:
        a, b = match.group()[4:-1].split(',')
        s += int(a) * int(b)
print(s)
