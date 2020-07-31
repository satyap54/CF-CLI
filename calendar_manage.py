from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import pickle
import json
from datetime import datetime, timedelta

def oauth_setup():
	scopes = ["https://www.googleapis.com/auth/calendar.events", 
	"https://www.googleapis.com/auth/calendar.readonly"]

	#path to client auth token
	path = os.path.join(".", "assets", "client_secret.json")
	flow = InstalledAppFlow.from_client_secrets_file(path, scopes = scopes)

	credentials = flow.run_console()

	with open(os.path.join(".", "assets", "token.pkl"), "wb") as f:
		pickle.dump(credentials, f)

def create_event(contest):
	credentials = pickle.load(open(os.path.join(".", "assets", "token.pkl"), "rb"))
	service = build("calendar", "v3", credentials = credentials)

	#result = service.calendarList().list().execute()
	#print(json.dumps(result))
	#calendar_id = result["items"][0]["id"]

	contest_name = contest["name"]
	start_time = datetime.fromtimestamp(int(contest["startTimeSeconds"])) 
	duration = contest["durationSeconds"]
	end_time = start_time + timedelta(seconds = int(duration))
	timeZone = "Asia/Kolkata"

	# Refer to the Python quickstart on how to setup the environment:
	# https://developers.google.com/calendar/quickstart/python

	event = {
		'summary': contest_name,
		'description': f"{contest['type']} {contest['id']} {start_time}",
		'start': {
			'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
			'timeZone': timeZone,
		},
		'end': {
			'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
			'timeZone': timeZone,
		},
		'reminders': {
			'useDefault': False,
			'overrides': [
			{'method': 'popup', 'minutes': 2880},
			],
		},
	}

	service.events().insert(calendarId = 'primary', body = event).execute()
