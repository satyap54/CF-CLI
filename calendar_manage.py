from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import pickle

def oauth_setup():
	scopes = ["https://www.googleapis.com/auth/calendar.events", 
	"https://www.googleapis.com/auth/calendar.readonly"]

	#path to client auth token
	path = os.path.join(".", "assets", "client_secret.json")
	flow = InstalledAppFlow.from_client_secrets_file(path, scopes = scopes)

	credentials = flow.run_console()

	with open(os.path.join(".", "assets", "token.pkl"), "wb") as f:
		pickle.dump(credentials, f)

def create_event():
	credentials = pickle.load(open(os.path.join(".", "assets", "token.pkl"), "rb"))
	service = build("calendar", "v3", credentials = credentials)
	
	result = service.calendarList().list().execute()
	print(result)