
import re


with open('day-3/input/part-1.txt') as f:
    file_content = f.read()


pattern = re.compile(r'mul\(\d+,\d+\)')

s = 0
muls = re.findall(pattern, file_content)
for mul in muls:
    a, b = mul[4:-1].split(',')
    s += int(a) * int(b)
print(s)
