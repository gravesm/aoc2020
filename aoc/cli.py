import click

from aoc import app


@click.group()
def main():
    pass


@main.command(name="1")
@click.argument("data", type=click.File("r"), default="-")
def day1(data):
    """Run day 1"""
    data = data.read().split()
    click.echo(app.day1(map(int, data)))
    click.echo(app.day1(map(int, data), r=3))


@main.command(name="2")
@click.argument("data", type=click.File("r"), default="-")
def day2(data):
    """Run day 2"""
    count_1 = 0
    count_2 = 0
    data = data.read().strip()
    for entry in data.splitlines():
        parts = app.parse_pw_entry(entry)
        valid = app.valid_pw(app.policy_1, *parts)
        if valid: count_1 += 1
        valid = app.valid_pw(app.policy_2, *parts)
        if valid: count_2 += 1
    click.echo(count_1)
    click.echo(count_2)
