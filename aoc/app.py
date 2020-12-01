from functools import reduce
from itertools import permutations
import operator


def day1(nums, r=2):
    for perm in permutations(nums, r=r):
        if reduce(operator.add, perm) == 2020:
            return reduce(operator.mul, perm)
