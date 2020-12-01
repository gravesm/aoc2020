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
