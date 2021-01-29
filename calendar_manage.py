from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
import json
from datetime import datetime, timedelta

def oauth_setup():
	SCOPES = ["https://www.googleapis.com/auth/calendar.events", 
	"https://www.googleapis.com/auth/calendar.readonly"]

	creds = None
	token_path = os.path.join(".", "assets", "token.pkl")
	cred_json_path = os.path.join(".", "assets", "credentials.json")

	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists(token_path):
		with open(token_path, 'rb') as token:
			creds = pickle.load(token)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				cred_json_path, SCOPES)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open(token_path, 'wb') as token:
			pickle.dump(creds, token)

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
