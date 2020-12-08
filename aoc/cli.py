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
        if valid:
            count_1 += 1
        valid = app.valid_pw(app.policy_2, *parts)
        if valid:
            count_2 += 1
    click.echo(count_1)
    click.echo(count_2)


@main.command(name="3")
@click.argument("data", type=click.File("r"), default="-")
def day3(data):
    """Run day 3"""
    click.echo(app.slope(data, 3, 1))
    total = 1
    for s in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        data.seek(0)
        total *= app.slope(data, *s)
    click.echo(total)


@main.command(name="4")
@click.argument("data", type=click.File("r"), default="-")
def day4(data):
    """Run day 4"""
    passports = list(app.make_passports(data.read().split("\n\n")))
    has_required = list(filter(app.pp_required_fields, passports))
    click.echo(len(has_required))
    is_valid = list(filter(app.pp_valid_fields, has_required))
    click.echo(len(is_valid))


@main.command(name="5")
@click.argument("data", type=click.File("r"), default="-")
def day5(data):
    tbl = str.maketrans(
        {ord("F"): ord("0"), ord("B"): ord("1"), ord("L"): ord("0"), ord("R"): ord("1")}
    )
    tickets = []
    for ticket in data:
        idx = min([ticket.index(c) for c in "LR" if c in ticket])
        row = app.bsearch(range(0, 128), ticket[0:idx].translate(tbl))
        col = app.bsearch(range(0, 8), ticket[idx:].translate(tbl))
        tickets.append(row * 8 + col)
    tickets.sort()
    click.echo(tickets[-1])
    for i, t in enumerate(tickets):
        if tickets[i + 1] - t != 1:
            click.echo(t + 1)
            return
