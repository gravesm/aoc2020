from functools import reduce
from itertools import permutations
import operator
import re


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
        lineln = len(line)
        if line[pos % lineln] == "#":
            trees += 1
    return trees


def make_passports(passports):
    for passport in passports:
        passport = passport.split()
        yield dict([field.split(":") for field in passport])


def pp_required_fields(passport):
    required = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}
    return set(passport.keys()) >= required


def pp_valid_fields(passport):
    try:
        assert (
            (1920 <= int(passport["byr"]) <= 2002)
            and (2010 <= int(passport["iyr"]) <= 2020)
            and (2020 <= int(passport["eyr"]) <= 2030)
        )
        m = re.match(r"^(\d+)(in|cm)$", passport["hgt"])
        if m.group(2) == "in":
            assert 59 <= int(m.group(1)) <= 76
        if m.group(2) == "cm":
            assert 150 <= int(m.group(1)) <= 193
        assert re.match(r"^#[\dabcdef]{6}$", passport["hcl"])
        assert passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        assert re.match(r"^\d{9}$", passport["pid"])
    except Exception:
        return False
    return True
