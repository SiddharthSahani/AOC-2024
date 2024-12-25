
from math import floor


with open('day-22/input/part-1.txt') as f:
    secrets = [int(line) for line in f.read().splitlines()]


def get_next(x):
    x ^= x * 64
    x %= 16777216
    x ^= floor(x / 32)
    x %= 16777216
    x ^= x * 2048
    x %= 16777216
    return x


def simulate(x, n):
    for _ in range(n):
        x = get_next(x)
    return x


s = sum(
    simulate(secret, 2000)
    for secret in secrets
)
print(s)
