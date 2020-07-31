import requests as rq
import json
import os

json_file_path = os.path.join(".", "assets", "contests_details.json")

def create_contest_details_json(include_gym = "false", usr_token = None):
	"""Create a JSON file containing details of upcoming contests"""

	payload = {"gym" : include_gym, "usr_token" : usr_token}
	contests_list = json.loads(
		(rq.get("https://codeforces.com/api/contest.list", data = payload)).text
	)

	with open(json_file_path, "w+") as f:
		json.dump(contests_list, f, indent = 4)