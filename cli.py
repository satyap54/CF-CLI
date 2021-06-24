import click,json
from click import parser
from tabulate import tabulate
from set_reminder import set_reminder
from user_data import user_data
from contest_data import contest_data
from robobrowser import RoboBrowser


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
	
@main.command()
@click.argument("problem_id")
@click.argument("file_name")
def submit(problem_id, file_name):
	""" Submit solution file"""
	
	# login to codeforces
	browser = RoboBrowser(parser = "html.parser")
	browser.open('http://codeforces.com/enter')	

	enter_form = browser.get_form('enterForm')
	enter_form["handleOrEmail"] = "KatZura"
	enter_form["password"] = "ydemtr,123"

	res = browser.submit_form(enter_form)
	enter_form = browser.get_form('enterForm')
	print("Logged In")
	
	browser.open('http://codeforces.com/problemset/submit')
	submit_form = browser.get_form(class_ = 'submit-form')
	submit_form['submittedProblemCode'] = problem_id
	try:
		submit_form['sourceFile'] = file_name
	except Exception as e:
		print("File not found in current dir")
		return
	
	browser.submit_form(submit_form)
	# check if the submission is done successfully	
	#print(browser.url)
	
	