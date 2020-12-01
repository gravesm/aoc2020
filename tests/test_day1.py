from click.testing import CliRunner

from aoc import app, cli


def test_day1_app():
    data = [1721, 979, 366, 299, 675, 1456]
    assert app.day1(data) == 514579
    assert app.day1(data, r=3) == 241861950


def test_day1_cli():
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
