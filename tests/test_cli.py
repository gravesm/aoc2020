from click.testing import CliRunner

from aoc import cli


def test_day1():
    data = """
        1721
        979
        366
        299
        675
        1456
    """
    runner = CliRunner()
    result = runner.invoke(cli.day1, input=data)
    assert result.output == "514579\n241861950\n"


def test_day2():
    data = """
        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc
    """
    runner = CliRunner()
    result = runner.invoke(cli.day2, input=data)
    assert result.output == "2\n1\n"


def test_day3():
    runner = CliRunner()
    result = runner.invoke(cli.day3, ["tests/fixtures/input3"])
    assert result.output == "7\n336\n"


def test_day4():
    runner = CliRunner()
    result = runner.invoke(cli.day4, ["tests/fixtures/input4"])
    assert result.output == "2\n2\n"


def test_day5():
    runner = CliRunner()
    result = runner.invoke(cli.day5, ["tests/fixtures/input5"])
    assert result.output.startswith("820")
