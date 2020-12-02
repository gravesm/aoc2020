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
