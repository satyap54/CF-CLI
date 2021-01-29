import click
from set_reminder import set_reminder

@click.command()
@click.option('--reminder', '-r', nargs = 0, help = "Set a reminder of next CodeForces Round")

def cli(reminder):
	set_reminder()
