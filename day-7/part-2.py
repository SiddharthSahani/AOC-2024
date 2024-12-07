
from itertools import product


with open('day-7/input/part-2.txt') as f:
    lines = f.read().splitlines()


def is_valid(test_val, nums):
    l = len(nums)
    for operators in product('+*|', repeat=l-1):
        res = 0
        for i, o in enumerate(operators, start=1):
            old = nums[0] if i == 1 else res

            if o == '+':
                res = old + nums[i]
            elif o == '*':
                res = old * nums[i]
            else:
                res = int(f"{old}{nums[i]}")

        if test_val == res:
            return True

    return False


res = 0

for line in lines:
    test_val, nums = line.split(': ')
    test_val = int(test_val)
    nums = [int(num) for num in nums.split(' ')]

    if is_valid(test_val, nums):
        res += test_val

print(res)
