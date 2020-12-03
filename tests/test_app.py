from aoc.app import day1, valid_pw, parse_pw_entry, policy_1, policy_2, slope


def test_day1_app():
    data = [1721, 979, 366, 299, 675, 1456]
    assert day1(data) == 514579
    assert day1(data, r=3) == 241861950


def test_validate_pw():
    assert valid_pw(policy_1, "abcde", "a", 1, 3) is True
    assert valid_pw(policy_1, "cdefg", "b", 1, 3) is False
    assert valid_pw(policy_1, "ccccccccc", "c", 2, 9) is True
    assert valid_pw(policy_2, "abcde", "a", 1, 3) is True
    assert valid_pw(policy_2, "cdefg", "b", 1, 3) is False
    assert valid_pw(policy_2, "ccccccccc", "c", 2, 9) is False


def test_parse_pw_entry():
    assert parse_pw_entry("1-3 a: abcde") == ("abcde", "a", 1, 3)


def test_slope():
    with open("tests/fixtures/input3") as fp:
        assert slope(fp, 3, 1) == 7
        fp.seek(0)
        assert slope(fp, 1, 1) == 2
        fp.seek(0)
        assert slope(fp, 5, 1) == 3
        fp.seek(0)
        assert slope(fp, 7, 1) == 4
        fp.seek(0)
        assert slope(fp, 1, 2) == 2
