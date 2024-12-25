
from math import floor


with open('day-22/input/part-2.txt') as f:
    secrets = [int(line) for line in f.read().splitlines()]


def get_next(x):
    x ^= x * 64
    x %= 16777216
    x ^= floor(x / 32)
    x %= 16777216
    x ^= x * 2048
    x %= 16777216
    return x


def gen_sequence(x):
    res = {}

    s = ()
    for _ in range(4):
        next_x = get_next(x)
        s += (next_x%10 - x%10,)
        x = next_x

    res[s] = x % 10

    i = 4
    while i < 2000:
        next_x = get_next(x)
        s = s[1:] + (next_x % 10 - x % 10,)
        if s not in res:
            res[s] = next_x % 10
        x = next_x
        i += 1

    return res


secret_sequences = [
    gen_sequence(x)
    for x in secrets
]

possible_seq = set()
for seq in secret_sequences:
    possible_seq.update(seq)

best_seq = max(
    possible_seq,
    key=lambda seq: sum(d.get(seq, 0) for d in secret_sequences)
)

print(sum(
    thing.get(best_seq, 0)
    for thing in secret_sequences
))
