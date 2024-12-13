
with open('day-13/input/part-2.txt') as f:
    sections = f.read().split('\n\n')


def get_cost(section):
    a_line, b_line, prize_line = section.splitlines()

    a_line = a_line.split(': ')[1].split(', ')
    a = (int(a_line[0][1:]), int(a_line[1][1:]))
    b_line = b_line.split(': ')[1].split(', ')
    b = (int(b_line[0][1:]), int(b_line[1][1:]))
    prize_line = prize_line.split(': ')[1].split(', ')
    p = (int(prize_line[0][2:]) + 10000000000000, int(prize_line[1][2:]) + 10000000000000)

    # a[0] * x + b[0] * y = p[0]
    # a[1] * x + b[1] * y = p[1]
    x = (p[0] * b[1] - p[1] * b[0]) / (a[0] * b[1] - a[1] * b[0])
    y = (p[1] * a[0] - p[0] * a[1]) / (a[0] * b[1] - a[1] * b[0])

    if x.is_integer() and y.is_integer():
        return int(x) * 3 + int(y) * 1
    return 0


s = sum(
    get_cost(section)
    for section in sections
)
print(s)
