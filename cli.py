import click,json
from click import parser
from tabulate import tabulate
from scripts.set_reminder import set_reminder
from scripts.user_data import user_data, get_latest_verdict
from scripts.contest_data import contest_data
from robobrowser import RoboBrowser
import time
import config


_verdict_unexpected = set(("REJECTED", "INPUT_PREPARATION_CRASHED", "CRASHED", "SECURITY_VIOLATED", "PRESENTATION_ERROR",
						"SKIPPED", "INPUT_PREPARATION_CRASHED"))
						
_verdict_end = set(("TIME_LIMIT_EXCEEDED", "MEMORY_LIMIT_EXCEEDED", "IDLENESS_LIMIT_EXCEEDED", "OK", "FAILED", "WRONG_ANSWER"))


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
@click.argument("contest_id")
@click.argument("problem_id")
@click.argument("file_name")
def submit(contest_id, problem_id, file_name):
	""" Submit solution file"""
	
	# login to codeforces
	browser = RoboBrowser(parser = "html.parser")
	browser.open('http://codeforces.com/enter')	

	enter_form = browser.get_form('enterForm')
	enter_form["handleOrEmail"] = config.USER_HANDLE
	enter_form["password"] = config.PASSWORD

	res = browser.submit_form(enter_form)
	enter_form = browser.get_form('enterForm')
	click.secho("Logged In", fg="green")
	
	browser.open(f'https://codeforces.com/contest/{contest_id}/submit/{problem_id}')
	submit_form = browser.get_form(class_ = 'submit-form')
	try:
		submit_form['sourceFile'] = file_name
	except Exception as e:
		click.secho("File not found in current dir", fg="red")
		return
	
	browser.submit_form(submit_form)
	# check if the submission is done successfully	
	#print(browser.url)
	if(browser.url.find("my") == -1):
		click.secho("Your submission has some problems.\n1)Check if you re-submitted the same solution\n2)Proper class-name for java solution\n3)OJ property", fg='blue')
		return

	click.secho(f"Submitted {file_name} for problem {problem_id}...", fg="yellow")
	click.echo("Testing...")

	final_res = None
	while True:
		res = get_latest_verdict(config.USER_HANDLE)
		if(res['verdict'] in _verdict_end):
			final_res = res
			break
		time.sleep(0.5)
		
	click.secho("Done!\n", fg="green")
	#print(tabulate(final_res, headers="keys"))
	click.secho(final_res["verdict"], fg=("green" if final_res["verdict"] == "OK" else "red"))
	click.secho(f"Solution Link: https://codeforces.com/contest/{contest_id}/submission/{final_res['id']}", fg="cyan")
	click.secho(f"Exec. Time: {final_res['time']} ms", fg="cyan")
	click.secho(f"Memory consm.: {final_res['memory']} KB", fg="cyan")
	click.secho(f"Ran on {final_res['passedTests']} tests", fg="cyan")