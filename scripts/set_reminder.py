from . import serialize
from . import calendar_manage
import json
import os
import click

def find_next_contest(li):
	l = 0
	r = len(li) - 1
	mid = None
	res = None

	while(l <= r):
		mid = l + (r  - l)//2

		if(li[mid]["phase"] == "BEFORE"):
			res = mid
			l = mid + 1
		else:
			r = mid - 1

	if(res == None):
		return -1
	else:
		return res

def set_reminder():

	if(not os.path.exists(os.path.join("..", "assets", "token.pkl"))):
		calendar_manage.oauth_setup()

	#Uncomment below line to update contest_details.json
	serialize.create_contest_details_json()
	
	try:
		with open(serialize.json_file_path, "r") as f:
			data = json.load(f)
			#print(data["result"])
			idx = find_next_contest(data["result"])

			if(idx == -1):
				click.echo("No upcoming contests")
			else:
				contest = data["result"][idx]
				click.echo(json.dumps(contest))
				calendar_manage.create_event(contest)
				
	except FileNotFoundError:
		click.echo("contests_details.json file is not present inside assets directory")

	finally:
		pass