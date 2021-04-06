import click,json
from tabulate import tabulate
from set_reminder import set_reminder
from user_data import user_data
from contest_data import contest_data

@click.group()
def main():
	pass

@main.command()
def remind():
	""" Set a reminder of next CodeForces Round """
	set_reminder()

@main.command()
@click.argument("users", nargs = -1)
def users(users):
	""" Gives information about one user or several users"""
	response = user_data(users)
	print("\tStatus :", response.status_code, response.reason, "\n")
	data = json.loads(response.text)
	data_list = []
	if(response.ok):
		for user_ob in data["result"]:
			li = []
			if(not "first_name" in user_ob):
				li.append(user_ob["handle"])
			else:
				li.append(f'{user_ob["firstName"]} {user_ob["lastName"]} aka {user_ob["handle"]}')
				
			li.append(user_ob["rating"])
			li.append(user_ob["maxRating"])
			li.append(user_ob["maxRank"])
			li.append(f'Friend of {user_ob["friendOfCount"]} users')

			data_list.append(li)
	
	headers = ["User", "Current Rating", "Max. Rating", "Max. Rank:", "Social"]
	print(tabulate(data_list, headers=headers))

@main.command()
@click.argument("contest", nargs = 1)
def contest(contest):
	""" Gives the number of problems and their difficulty in a contest """
	response = contest_data(contest)
	print("\tStatus :", response.status_code, response.reason, "\n")
	data = json.loads(response.text)
