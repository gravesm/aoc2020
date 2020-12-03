from functools import reduce
from itertools import permutations
import operator


def day1(nums, r=2):
    for perm in permutations(nums, r=r):
        if reduce(operator.add, perm) == 2020:
            return reduce(operator.mul, perm)


def parse_pw_entry(entry):
    parts = entry.split()
    first, second = parts[0].split("-")
    char = parts[1][0]
    pw = parts[2]
    return pw, char, int(first), int(second)


def valid_pw(policy, pw, char, first, second):
    return policy(pw, char, first, second)


def policy_1(pw, char, first, second):
    return first <= pw.count(char) <= second


def policy_2(pw, char, first, second):
    return (pw[first - 1] == char) != (pw[second - 1] == char)


def slope(data, x, y):
    lineno = 0
    pos = 0
    trees = 0
    for line in data:
        if (lineno < y) or (lineno % y):
            lineno += 1
            continue
        line = line.strip()
        lineno += 1
        pos += x
        while len(line) <= pos:
            line += line
        if line[pos] == "#":
            trees += 1
    return trees
