import click,json
from set_reminder import set_reminder
from user_data import user_data

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
	if(response.ok):
		for user_ob in data["result"]:
			print(f'{user_ob["firstName"]} {user_ob["lastName"]} aka {user_ob["handle"]}')
			print("Current Rating: ",user_ob["rating"])
			print("Max. Rating: ", user_ob["maxRating"])
			print("Max. Rank: ", user_ob["maxRank"])
			print("\n")
